import json
from options import *
from messages import MESSAGES
from typing import List, Set

def apply_wordle_filter(hints_list: List[str], valid_words: Set[str]) -> List[str]:
    filtered = set(valid_words)
    new_filtered = set()
    letter_count = dict()
    correct_letters_location = dict()
    existing_letters = set()

    for hints in hints_list:
        j = 0
        hint_letters = list()
        for i, char in enumerate(hints):
            if char == wildcard or char == nel:
                continue

            #not found in the word
            elif char.isalpha() and hints[i-1] == nel:
                j = j + 1
                if(char not in letter_count):
                    letter_count[char.lower()] = -1
                continue

            #found and correct position
            elif char.isupper():
                correct_letters_location[j] = char.lower()
                existing_letters.add(char.lower())
                hint_letters.append(char)
                j = j + 1
            
            #found but wrong position
            elif char.islower():
                existing_letters.add(char)
                hint_letters.append(char)
                j = j + 1

            if(char in letter_count and (hint_letters.count(char) > letter_count[char] or letter_count[char] == -1)):
                letter_count[char.lower()] = hint_letters.count(char)
            else:
                letter_count[char.lower()] = hint_letters.count(char)
    
    for word in filtered:
        match = True

        for char in word:
            if(char in letter_count and (word.count(char) < letter_count[char] or letter_count[char] < 0)):
                match = False
                break

            if(word.index(char) in correct_letters_location and char != correct_letters_location[word.index(char)]):
                match = False
                break

            for existing_char in existing_letters:
                if(word.count(existing_char) == 0):
                    match = False
                    break
        
        if(match == True):
            new_filtered.add(word)
    
    filtered = sorted(new_filtered)

    return list(filtered)            

def main() -> None:
    
    lang = input(MESSAGES["en"]["choose_language"]).strip().lower()
    if lang not in OPTIONS["languages"]:
        print(MESSAGES["en"]["invalid_language"])
        lang = "en"  # Default to English

    print(MESSAGES[lang]["loading_words"])

    file_name = f"languages/{lang}.json"
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            valid_words = set(json.load(file))
    except Exception as e:
        print(f"Error loading JSON file: {e}")

    print(MESSAGES[lang]["welcome"] + "\n")
    print(MESSAGES[lang]["patterns"] + "\n")
    print(MESSAGES[lang]["choose_pattern"])

    while True:
        user_input: str = input("> ").strip()
        if user_input.lower() in {"0"}:
            print(MESSAGES[lang]["goodbye"])
            break
        elif not user_input:
            print(MESSAGES[lang]["invalid_input"])
            continue

        hints_list = [hint.strip() for hint in user_input.split(",") if hint.strip()]

        words_that_fit = apply_wordle_filter(hints_list, valid_words)
        if words_that_fit:
            print(MESSAGES[lang]["matches_found"].format(count=len(words_that_fit)))
            print(', '.join(words_that_fit))
        else:
            print(MESSAGES[lang]["no_matches"])

if __name__ == "__main__":
    main()