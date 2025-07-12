import random

def generate_quote():
    quotes = [
        "Be yourself; everyone else is already taken. — Oscar Wilde",
        "You only live once, but if you do it right, once is enough. — Mae West",
        "In the middle of every difficulty lies opportunity. — Albert Einstein",
        "It does not matter how slowly you go as long as you do not stop. — Confucius",
        "Happiness is not something ready made. It comes from your own actions. — Dalai Lama",
        "Turn your wounds into wisdom. — Oprah Winfrey",
        "Every moment is a fresh beginning. — T.S. Eliot",
        "Believe you can and you're halfway there. — Theodore Roosevelt",
        "Do what you can, with what you have, where you are. — Theodore Roosevelt",
        "Dream big and dare to fail. — Norman Vaughan",
    ]

    quote = random.choice(quotes)
    print("\n🌟 Beautiful Quote of the Moment:\n")
    print(f"\"{quote}\"\n")

# Run the quote generator
generate_quote()
