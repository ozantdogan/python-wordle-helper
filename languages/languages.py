import config.config as config
from colorama import Fore, Style
from languages.strings import MESSAGES, DICTIONARY
import json
import requests
from requests.exceptions import RequestException
import re
ITALIC = "\033[3m"
RESET = "\033[0m"

def select():
    choose_language_message = ""
    for lang in config.APP_SETTINGS["languages"]:
        lang = str(lang)
        choose_language_message += Fore.CYAN + f"[{lang.lower()}] " + MESSAGES[lang]["choose_language"] + Style.RESET_ALL + "\n"

    lang = input(choose_language_message + "> ").strip().lower()
    if lang not in config.APP_SETTINGS["languages"]:
        print(Fore.RED + MESSAGES["en"]["invalid_language"] + Style.RESET_ALL)
        lang = "en"

    return lang

def load(lang):
    file_name = f"languages/data/{lang}.json"
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            valid_words = set(json.load(file))
    except Exception as e:
        print(Fore.RED + f"Error loading JSON file: {e}" + Style.RESET_ALL)
    
    return valid_words

def get_meaning(word: str, lang):
    url = DICTIONARY.get(lang, "")
    if not url:
        return ""
    
    if lang == "en":
        return get_english_meaning(word, url)
    elif lang == "tr":
        return get_turkish_meaning(word, url)
    

def get_english_meaning(word, url):
    url = url.format(word=word)
    try:
        response = requests.get(url=url, timeout=5)  # Added timeout for better handling
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx and 5xx)
        data = response.json()
    except RequestException as e:
        return ""

    if "title" in data and data["title"] == "No Definitions Found":
        return f""

    formatted_text = ""
    count = 1

    for entry in data:
        meanings = entry.get("meanings", [])

        for meaning in meanings:
            word_type = meaning.get("partOfSpeech", "").lower()
            if(word_type == "noun"):
                word_type = "n."
            elif(word_type == "verb"):
                word_type = "v."
            elif(word_type == "adverb"):
                word_type = "adv."
            elif(word_type == "adjective"):
                word_type == "adj."

            definitions = meaning.get("definitions", [])
            
            for definition in definitions:
                formatted_text += f"{Fore.LIGHTBLACK_EX}{ITALIC}  {count}.({word_type}) {definition['definition']}{RESET}{Style.RESET_ALL}\n"
                example = definition.get("example")
                if example:
                    formatted_text += f"{Fore.LIGHTBLACK_EX}{ITALIC}    [e.g.] {example}{RESET}{Style.RESET_ALL}\n"
                count += 1

    return formatted_text.strip()

def get_turkish_meaning(word, url):
    url = url.format(word=word)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Connection": "close"
    }

    try:
        response = requests.get(url=url, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()
    except RequestException as e:
        print(e)
        return 
    
    if "sonuç bulunamadı" in response.text.lower():
        return f""
    
    formatted_text = ""
    count = 1
    
    for entry in data:  # Iterate over dictionary values
        meanings = entry.get("anlamlarListe", [])

        for meaning in meanings:
            # Extract word type (e.g., noun, verb)
            word_types = meaning.get("ozelliklerListe", [])
            if word_types:
                previous_word_type = ", ".join([wt.get("tam_adi", "").lower() for wt in word_types])
            word_type = previous_word_type

            # Extract the definition
            definition = meaning.get("anlam", "")

            # Format output
            formatted_text += f"{Fore.LIGHTBLACK_EX}{ITALIC}  {count}. ({word_type}) {definition}{RESET}{Style.RESET_ALL}\n"

            # Extract example sentences
            examples = meaning.get("orneklerListe", [])
            for example in examples:
                example_text = example.get("ornek", "")
                if example_text:
                    formatted_text += f"{Fore.LIGHTBLACK_EX}{ITALIC}    [örn.] {example_text}{RESET}{Style.RESET_ALL}\n"

            count += 1

    return formatted_text.strip()
    


