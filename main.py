import json
from options import *
from messages import MESSAGES
from typing import List, Set

def apply_wordle_filter(hints_list: List[str], valid_words: Set[str]) -> List[str]:
    filtered = set(valid_words)

    for hints in hints_list:
        included_letters = set()  
        excluded_letters = set()  
        new_filtered = set()

        i = 0
        while i < len(hints):
            if hints[i] == nel:
                if i + 1 < len(hints) and hints[i + 1].isalpha():
                    excluded_letters.add(hints[i + 1].lower())  
                    i += 1  
            i += 1

        for i, char in enumerate(hints):
            if char == wildcard or char.lower() in excluded_letters:
                continue  
            elif char.isupper():
                included_letters.add(char.lower())  
            elif char.islower():
                included_letters.add(char) 

        for word in filtered:
            match = True

            if not all(letter in word for letter in included_letters):
                continue

            if any(letter in word for letter in excluded_letters):
                continue

            i = -1
            for j, char in enumerate(hints):
                if char == wildcard or char == nel:
                    continue  
                elif char.isupper() and hints[j-1] != nel:
                    i += 1
                    if word[i] != char.lower(): 
                        match = False
                        break
                elif char.islower() or hints[j-1] == nel:  
                    i += 1
                    if word[i] == char:  
                        match = False
                        break

            if match:
                new_filtered.add(word)

        filtered = new_filtered  

    return list(filtered)


def main() -> None:
    
    lang = input(MESSAGES["en"]["choose_language"]).strip().lower()
    if lang not in {"en", "tr"}:
        print(MESSAGES["en"]["invalid_language"])
        lang = "en"  # Default to English

    print(MESSAGES[lang]["loading_words"])

    file_name = f"languages/{lang}.json"
    with open(file_name, 'r', encoding='utf-8') as file:
        valid_words = set(json.load(file))

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