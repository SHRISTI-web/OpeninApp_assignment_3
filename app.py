import sys
sys.stdout.reconfigure(encoding='utf-8')

translations = {
    "Definitely": "मझु ेसि",
    "share": "इस्तमे  ाल करनेके लि े",
    "feedback": "प्रतिक्रिया",
    "comment": "टिप्पणी",
    "So": "तो",
    "big": "बड़ा",
    "video": "वीडियो",
    "clearly": "स्पष  रूपसे",
    "mention": "उल्लेख करना",
    "products": "उत्पाद",
    "waiting": "इंतजार",
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
