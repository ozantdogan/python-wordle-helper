from config.config import APP_SETTINGS
from colorama import Fore, Style
from languages.strings import MESSAGES
import json

def select():
    choose_language_message = ""
    for lang in APP_SETTINGS["languages"]:
        lang = str(lang)
        choose_language_message += Fore.CYAN + f"[{lang.upper()}] " + MESSAGES[lang]["choose_language"] + Style.RESET_ALL + "\n"

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