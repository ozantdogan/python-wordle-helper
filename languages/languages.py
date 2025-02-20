from config.config import APP_SETTINGS
from colorama import Fore, Style
from languages.strings import MESSAGES, DICTIONARY
import json
import requests

def select():
    choose_language_message = ""
    for lang in APP_SETTINGS["languages"]:
        lang = str(lang)
        choose_language_message += Fore.CYAN + f"[{lang.lower()}] " + MESSAGES[lang]["choose_language"] + Style.RESET_ALL + "\n"

    lang = input(choose_language_message + "> ").strip().lower()
    if lang not in APP_SETTINGS["languages"]:
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

ITALIC = "\033[3m"
RESET = "\033[0m"

def get_meaning(word: str, lang):
    url = DICTIONARY.get(lang, "")
    if not url:
        return ""
    
    if lang == "en":
        url = url.format(word=word)
        response = requests.get(url=url)
        data = response.json()

        if "title" in data and data["title"] == "No Definitions Found":
            return f""

        formatted_text = ""
        count = 1

        for entry in data:
            meanings = entry.get("meanings", [])

            for meaning in meanings:
                part_of_speech = meaning.get("partOfSpeech", "").lower()
                definitions = meaning.get("definitions", [])
                
                for definition in definitions:
                    formatted_text += f"{Fore.LIGHTBLACK_EX}{ITALIC}  {count}.({part_of_speech}) {definition['definition']}{RESET}{Style.RESET_ALL}\n"
                    example = definition.get("example")
                    if example:
                        formatted_text += f"   {Fore.LIGHTBLACK_EX}{ITALIC}(e.g.){example}{RESET}{Style.RESET_ALL}\n"
                    count += 1

        return formatted_text.strip()

