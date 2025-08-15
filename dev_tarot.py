import random
import os
import time

def load_cards(lang):
    path = os.path.join("cards", f"{lang}.txt")
    with open(path, encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

def choose_language():
    print("🌐 Choose your language / Выберите язык:")
    print("1. English")
    print("2. Русский")
    choice = input("Enter 1 or 2: ")
    return "ru" if choice == "2" else "en"

def draw_card(cards, lang):
    print("\n🔮 Shuffling the deck..." if lang == "en" else "\n🔮 Перемешиваем колоду...")
    time.sleep(1.5)
    card = random.choice(cards)
    print("\n🃏 Your Dev Tarot card:" if lang == "en" else "\n🃏 Ваша карта Dev Tarot:")
    print(f"» {card} «\n")

def main():
    lang = choose_language()
    cards = load_cards(lang)
    draw_card(cards, lang)

if __name__ == "__main__":
    main()
