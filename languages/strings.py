from config.config import *

MESSAGES = {
    "en": {
        "welcome": "Welcome to Wordle Helper!",
        "patterns": f"• {nel}[letter]: A letter that does not exist in the word at all.\n• [lowercase_letter]: A letter that exists in the word but is in the wrong position.\n• [uppercase_letter]: A letter that is in the correct position in the word.",        
        "choose_pattern": f"Enter your word pattern(s) separated by commas (e.g., {nel}b{nel}aK{nel}e{nel}r,{nel}tOw{nel}e{nel}l):",
        "invalid_input": "Invalid input. Please enter a word pattern.",
        "no_matches": "No matching words found.",
        "matches_found": "Possible words ({count} matches):",
        "goodbye": "Goodbye!",
        "choose_language": f"Choose language",
        "invalid_language": "Invalid choice. Defaulting to English...",
        "loading_words": "Loading word list...",
        "word_not_found": "Word not found.",
        "word_must_have_5_letters": "Word must have 5 letters.",
        "word_already_exists": "Word already exists.",
        "you_won": "You won! 🎉",
        "game_over": "Game over! Correct word: {answer}",
        "play_again": "Play again",
        "change_language": "Change language",
        "give_up": "Give up",
        "show_answer": "Show answer",
        "exit":"Exit",
        "clear_screen": "Clear screen"
    },
    "tr": {
        "welcome": "Wordle Yardımcısına Hoş Geldiniz!",
        "patterns": f"\n• {nel}[harf]: Kelimede hiç bulunmayan harf. Bu harf, kelimenin hiçbir yerinde yer almaz.\n• [küçük_harf]: Kelimede bulunan ancak yanlış konumda olan harf. Bu harf doğru konumda değil.\n• [büyük_harf]: Kelimede doğru konumda bulunan harf. Bu harf, kelimenin doğru pozisyonundadır.",        
        "choose_pattern": f"Kelime desen(ler)inizi virgülle ayırarak girin (örn. {nel}a{nel}ş{nel}uR{nel}e,{nel}e{nel}krA{nel}n):",
        "invalid_input": "Geçersiz giriş. Lütfen bir kelime deseni girin.",
        "no_matches": "Eşleşen kelime bulunamadı.",
        "matches_found": "Olası kelimeler ({count} eşleşme):",
        "goodbye": "Güle güle!",
        "choose_language": f"Dil seçin",
        "invalid_language": "Geçersiz seçim. Varsayılan olarak İngilizce seçildi...",
        "loading_words": "Kelime listesi yükleniyor...",
        "word_not_found": "Kelime bulunamadı.",
        "word_must_have_5_letters": "Kelime 5 harf içermelidir.",
        "word_already_exists": "Kelime bulunmakta.",
        "you_won": "Kazandın! 🎉",
        "game_over": "Oyun bitti! Doğru kelime: {answer}",
        "play_again": "Tekrar oyna",
        "change_language": "Dil değiştir",
        "give_up": "Pes et",
        "show_answer": "Cevabı göster",
        "exit":"Çıkış",
        "clear_screen": "Ekranı temizle"
    },
    "fr": {
        "welcome": "Bienvenue sur l'assistant Wordle !",
        "patterns": f"• {nel}[lettre] : Une lettre qui n'existe pas du tout dans le mot.\n• [lettre_minuscule] : Une lettre qui existe dans le mot mais est mal placée.\n• [LETTRE_MAJUSCULE] : Une lettre qui est bien placée dans le mot.",        
        "choose_pattern": f"Entrez votre ou vos modèles de mots, séparés par des virgules (ex. {nel}b{nel}oN{nel}j{nel}o{nel}u,{nel}pOu{nel}r{nel}q{nel}u):",
        "invalid_input": "Entrée invalide. Veuillez entrer un modèle de mot.",
        "no_matches": "Aucun mot correspondant trouvé.",
        "matches_found": "Mots possibles ({count} correspondances) :",
        "goodbye": "Au revoir !",
        "choose_language": f"Choisissez une langue",
        "invalid_language": "Choix invalide. L'anglais sera utilisé par défaut...",
        "loading_words": "Chargement de la liste des mots...",
        "word_not_found": "Mot non trouvé.",
        "word_must_have_5_letters": "Le mot doit contenir 5 lettres.",
        "word_already_exists":"Le mot existe déjà.",
        "you_won": "Vous avez gagné ! 🎉",
        "game_over": "Partie terminée ! Le mot correct était : {answer}",
        "play_again": "Rejouer",
        "change_language": "Changer de langue",
        "give_up": "Abandonner",
        "show_answer": "Afficher la réponse",
        "exit": "Quitter",
        "clear_screen": "Nettoyer l'écran"
    },
    "it": {
        "welcome": "Benvenuto in Wordle Helper!",
        "patterns": f"• {nel}[lettera]: Una lettera che non esiste affatto nella parola.\n• [lettera minuscola]: Una lettera che esiste nella parola ma è nella posizione sbagliata.\n• [LETTERA MAIUSCOLA]: Una lettera che è nella posizione corretta nella parola.",        
        "choose_pattern": f"Inserisci il tuo schema di parole separato da virgole (es. {nel}b{nel}aK{nel}e{nel}r,{nel}tOw{nel}e{nel}l):",
        "invalid_input": "Input non valido. Inserisci uno schema di parola.",
        "no_matches": "Nessuna parola corrispondente trovata.",
        "matches_found": "Parole possibili ({count} corrispondenze):",
        "goodbye": "Arrivederci!",
        "choose_language": "Scegli la lingua",
        "invalid_language": "Scelta non valida. Impostazione predefinita in italiano...",
        "loading_words": "Caricamento elenco parole...",
        "word_not_found": "Parola non trovata.",
        "word_must_have_5_letters": "La parola deve avere 5 lettere.",
        "word_already_exists": "La parola esiste già.",
        "you_won": "Hai vinto! 🎉",
        "game_over": "Game over! Parola corretta: {answer}",
        "play_again": "Gioca di nuovo",
        "change_language": "Cambia lingua",
        "give_up": "Mi arrendo",
        "show_answer": "Mostra risposta",
        "exit":"Esci",
        "clear_screen": "Schermo pulito"
    }
}

KEYBOARDS = {
    "en": ["qwertyuiop", "asdfghjkl", "zxcvbnm"],
    "tr": ["qwertyuıopğü", "asdfghjklşi", "zxcvbnmöç"],
    "fr": ["azertyuiop", "qsdfghjklm", "wxcvbn"],
    "it": ["qwertyuiop", "asdfghjklò", "zxcvbnm"]
}

DICTIONARY = {
    "en": "https://api.dictionaryapi.dev/api/v2/entries/en/{word}",
    "tr": "https://sozluk.gov.tr/gts?ara={word}"
}