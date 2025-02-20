import json
import colorama
from colorama import Fore, Style
from config.config import *
from languages import languages
from languages.strings import MESSAGES
from typing import List, Set, Dict
from collections import defaultdict, Counter

colorama.init(autoreset=True)  # Automatically resets color after each print

command_list = {
    "0": "clear_screen",
    "1": "change_language",
    "2": "exit",
}

lang = "en"
valid_words = set()

def compute_letter_frequencies(word_list: List[str]):
    """Computes letter frequency overall and per position."""
    letter_counts = Counter()
    position_counts = [Counter() for _ in range(len(next(iter(word_list), "_____")))]  # Default length 5

    for word in word_list:
        for i, letter in enumerate(word):
            letter_counts[letter] += 1
            position_counts[i][letter] += 1

    return letter_counts, position_counts

def compute_word_probability(word_list: List[str], letter_counts: Counter, position_counts: List[Counter]):
    """Assigns probabilities to words based on letter and position frequency."""
    word_scores = {}

    for word in word_list:
        score = 1.0  # Start with a neutral score

        for i, letter in enumerate(word):
            # Weigh by letter frequency
            letter_freq = letter_counts[letter] / sum(letter_counts.values())
            position_freq = position_counts[i][letter] / sum(position_counts[i].values())
            score *= letter_freq * position_freq  # Combine both factors

        word_scores[word] = score

    # Normalize to sum up to 1
    total_score = sum(word_scores.values())
    for word in word_scores:
        word_scores[word] /= total_score

    return word_scores

def apply_wordle_filter(hints_list: List[str], valid_words: Set[str]) -> List[str]:
    """Filters valid words based on hints."""
    filtered = set(valid_words)
    new_filtered = set()
    letter_count = dict()
    correct_letters_location = dict()
    used_letters_location = dict()
    existing_letters = set()
    non_existing_letters = set()

    for hints in hints_list:
        j = 0
        hint_letters = list()
        for i, char in enumerate(hints):
            if char == wildcard or char == nel:
                continue

            elif char.isalpha() and hints[i - 1] == nel:
                non_existing_letters.add(char)
                if(char not in letter_count):
                    letter_count[char.lower()] = -1
                j += 1

            elif char.isupper():
                correct_letters_location[j] = char
                existing_letters.add(char.lower())
                hint_letters.append(char)
                j += 1
            
            elif char.islower():
                used_letters_location[j] = char
                existing_letters.add(char)
                hint_letters.append(char)
                j += 1

            if(char in non_existing_letters):
                letter_count[char] = hint_letters.count(char)
            else:
                letter_count[char] = max(hint_letters.count(char), letter_count.get(char.lower(), 0))

    for word in filtered:
        match = True

        for i, char in enumerate(word):
            if any(word.lower().count(existing_char) == 0 for existing_char in existing_letters):
                match = False
                break

            if i in correct_letters_location and char.upper() != correct_letters_location[i]:
                match = False
                break
            elif i in correct_letters_location and char.upper() == correct_letters_location[i]:
                char = char.upper()
                word = word[:i] + word[i].upper() + word[i + 1:]

        for i, char in enumerate(word):
            if char in letter_count and (word.count(char) != letter_count[char] or letter_count[char] < 0):
                match = False
                break
            
            if i in used_letters_location and char == used_letters_location[i]:
                match = False
                break

        if match:
            new_filtered.add(word.lower())

    return sorted(new_filtered)

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

def load_words() -> set:
    global valid_words
    valid_words = languages.load(lang)

def apply_words(input: str, valid_words):
    hints_list = [hint.strip() for hint in input.split(",") if hint.strip()]

    words_that_fit = apply_wordle_filter(hints_list, valid_words)

    if words_that_fit:
        print(Fore.GREEN + MESSAGES[lang]["matches_found"].format(count=len(words_that_fit)) + Style.RESET_ALL)

        letter_counts, position_counts = compute_letter_frequencies(words_that_fit)
        word_probabilities = compute_word_probability(words_that_fit, letter_counts, position_counts)

        sorted_words = sorted(word_probabilities.items(), key=lambda x: x[1], reverse=True)

        formatted_output = ", ".join([f"{word}{Fore.LIGHTBLACK_EX}(%{prob*100:.2f}){Style.RESET_ALL}" for word, prob in sorted_words])
        print(formatted_output)

    else:
        print(Fore.RED + MESSAGES[lang]["no_matches"] + Style.RESET_ALL)

def apply_commands(input: str):
    global lang
    command = command_list[input]
    if command == "exit":
        print(Fore.MAGENTA + MESSAGES[lang]["goodbye"] + Style.RESET_ALL)
        return False
    elif command == "change_language":
        os.system('cls' if os.name == 'nt' else 'clear')
        lang = languages.select()
        load_words()
        print_screen()
    elif command == "clear_screen":
        print_screen()
    
    return True

def print_commands():
    for key, value in command_list.items():
        print(Fore.LIGHTBLACK_EX + f"{key}. {MESSAGES[lang][value]}" + Style.RESET_ALL)

def print_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.GREEN + MESSAGES[lang]["welcome"] + "\n" + Style.RESET_ALL)
    print(Fore.BLUE + MESSAGES[lang]["patterns"] + "\n" + Style.RESET_ALL)
    print_commands()
    print(Fore.CYAN + MESSAGES[lang]["choose_pattern"] + Style.RESET_ALL)

def main() -> None:
    run = True

    lang = languages.select()
    load_words()
    print_screen()

    while run:
        user_input: str = input("> ").strip()
        if user_input in command_list:
            run = apply_commands(user_input)
        else:
            apply_words(user_input, valid_words)

if __name__ == "__main__":
    main()

