import json
import colorama
from colorama import Fore, Style
from options import *
from messages import MESSAGES
from typing import List, Set, Dict
from collections import defaultdict

colorama.init(autoreset=True)  # Automatically resets color after each print

def apply_wordle_filter(hints_list: List[str], valid_words: Set[str]) -> List[str]:
    filtered = set(valid_words)
    new_filtered = set()
    letter_count = dict()
    correct_letters_location = dict()
    used_letters_location = defaultdict(set)
    existing_letters = set()

    for hints in hints_list:
        j = 0
        hint_letters = list()
        for i, char in enumerate(hints):
            if char == wildcard or char == nel:
                continue

            # Not found in the word
            elif char.isalpha() and hints[i - 1] == nel:
                j = j + 1
                if char not in letter_count:
                    letter_count[char.lower()] = -1
                continue

            # Found and correct position (Green)
            elif char.isupper():
                correct_letters_location[j] = char
                existing_letters.add(char.lower())
                hint_letters.append(char)
                j = j + 1
            
            # Found but wrong position (Yellow)
            elif char.islower():
                used_letters_location[char.lower()].add(j)
                existing_letters.add(char)
                hint_letters.append(char)
                j = j + 1

            if char in letter_count and (hint_letters.count(char) > letter_count[char] or letter_count[char] == -1):
                letter_count[char.lower()] = hint_letters.count(char)
            else:
                letter_count[char.lower()] = hint_letters.count(char)

    for word in filtered:
        match = True

        for i, char in enumerate(word):
            if char in letter_count and (word.count(char) < letter_count[char] or letter_count[char] < 0):
                match = False
                break

            if i in correct_letters_location and char.upper() != correct_letters_location[i]:
                match = False
                break

            for existing_char in existing_letters:
                if word.count(existing_char) == 0:
                    match = False
                    break
            
            if char in used_letters_location:
                char_positions = {i for i, c in enumerate(word) if c == char}
                if not char_positions.isdisjoint(used_letters_location[char]):
                    match = False
                    break    

        if match:
            new_filtered.add(word)

    filtered = sorted(new_filtered)
    return list(filtered)            

def colorize_word(word: str, correct_positions: Dict[int, str], used_positions: Dict[str, set]) -> str:
    """Colorizes a word based on correct (green) and misplaced (yellow) letters."""
    colored_word = ""
    for i, char in enumerate(word):
        if i in correct_positions and char.upper() == correct_positions[i]:
            colored_word += Fore.GREEN + char + Style.RESET_ALL
        elif char in used_positions and i in used_positions[char]:
            colored_word += Fore.YELLOW + char + Style.RESET_ALL
        else:
            colored_word += char
    return colored_word

def main() -> None:
    lang = input(Fore.CYAN + MESSAGES["en"]["choose_language"] + Style.RESET_ALL).strip().lower()
    if lang not in OPTIONS["languages"]:
        print(Fore.RED + MESSAGES["en"]["invalid_language"] + Style.RESET_ALL)
        lang = "en"  # Default to English

    print(Fore.YELLOW + MESSAGES[lang]["loading_words"] + Style.RESET_ALL)

    file_name = f"languages/{lang}.json"
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            valid_words = set(json.load(file))
    except Exception as e:
        print(Fore.RED + f"Error loading JSON file: {e}" + Style.RESET_ALL)
        return

    print(Fore.GREEN + MESSAGES[lang]["welcome"] + "\n" + Style.RESET_ALL)
    print(Fore.BLUE + MESSAGES[lang]["patterns"] + "\n" + Style.RESET_ALL)
    print(Fore.CYAN + MESSAGES[lang]["choose_pattern"] + Style.RESET_ALL)

    while True:
        user_input: str = input("> ").strip()
        if user_input.lower() in {"0"}:
            print(Fore.MAGENTA + MESSAGES[lang]["goodbye"] + Style.RESET_ALL)
            break
        elif not user_input:
            print(Fore.RED + MESSAGES[lang]["invalid_input"] + Style.RESET_ALL)
            continue

        hints_list = [hint.strip() for hint in user_input.split(",") if hint.strip()]
        words_that_fit = apply_wordle_filter(hints_list, valid_words)

        if words_that_fit:
            print(Fore.GREEN + MESSAGES[lang]["matches_found"].format(count=len(words_that_fit)) + Style.RESET_ALL)
            print(', '.join([colorize_word(word, {}, {}) for word in words_that_fit]))
        else:
            print(Fore.RED + MESSAGES[lang]["no_matches"] + Style.RESET_ALL)

if __name__ == "__main__":
    main()
