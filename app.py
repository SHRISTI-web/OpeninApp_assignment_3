import sys
sys.stdout.reconfigure(encoding='utf-8')

translations = {
    "Definitely": "अवश्य",
    "share": "साझा करें",
    "feedback": "प्रतिक्रिया",
    "comment": "टिप्पणी",
    "So": "तो",
    "big": "बड़ा",
    "video": "वीडियो",
    "clearly": "स्पष रूप से",
    "mention": "उल्लेख करना",
    "products": "उत्पाद",
    "waiting": "in इंतजार",
    "bag": "बैग",
}

statements = [
    "Definitely share your feedback in the comment section.",
    "So even if it's a big video, I will clearly mention all the products.",
    "I was waiting for my bag.",
]

def hinglish_translation(text):
     words = text.split()
     translated_words = [translations.get(word, word) for word in words]
     translated_text = " ".join(translated_words)
     return translated_text
translated_statements = [hinglish_translation(statement) for statement in statements]
for i, statement in enumerate(translated_statements, start=1):
    print(f"{i}. {statement}") 

