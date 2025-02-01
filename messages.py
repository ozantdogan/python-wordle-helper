from options import *

MESSAGES = {
    "en": {
        "welcome": "Welcome to Wordle Helper!",
        "patterns": f"• {nel}[letter]: A letter that does not exist in the word at all.\n• [lowercase_letter]: A letter that exists in the word but is in the wrong position.\n• [uppercase_letter]: A letter that is in the correct position in the word.",        
        "choose_pattern": f"Enter your word pattern(s) separated by commas (e.g., {nel}b{nel}aK{nel}e{nel}r,{nel}tOw{nel}e{nel}l), or type '0{exit_input}' to exit:",
        "invalid_input": "Invalid input. Please enter a word pattern.",
        "no_matches": "No matching words found.",
        "matches_found": "Possible words ({count} matches):",
        "goodbye": "Goodbye!",
        "choose_language": f"Choose language / Dil seçin ({languages}): ",
        "invalid_language": "Invalid choice. Defaulting to English...",
        "loading_words": "Loading word list...",
    },
    "tr": {
        "welcome": "Wordle Yardımcısına Hoş Geldiniz!",
        "patterns": f"\n• {nel}[letter]: Kelimede hiç bulunmayan harf. Bu harf, kelimenin hiçbir yerinde yer almaz.\n• [lowercase_letter]: Kelimede bulunan ancak yanlış konumda olan harf. Bu harf doğru konumda değil.\n• [uppercase_letter]: Kelimede doğru konumda bulunan harf. Bu harf, kelimenin doğru pozisyonundadır.",        
        "choose_pattern": f"Kelime desen(ler)inizi virgülle ayırarak girin (örn. {nel}a{nel}ş{nel}uR{nel}e,{nel}e{nel}krA{nel}n), çıkmak için '{exit_input}' yazın:",
        "invalid_input": "Geçersiz giriş. Lütfen bir kelime deseni girin.",
        "no_matches": "Eşleşen kelime bulunamadı.",
        "matches_found": "Olası kelimeler ({count} eşleşme):",
        "goodbye": "Güle güle!",
        "choose_language": f"Dil seçin / Choose language ({languages}): ",
        "invalid_language": "Geçersiz seçim. Varsayılan olarak İngilizce seçildi...",
        "loading_words": "Kelime listesi yükleniyor...",
    }
}
