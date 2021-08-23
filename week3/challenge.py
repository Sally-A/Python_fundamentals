import random

diamonds = ["AD", "2D", "3D", "4D", "5D", "6D",
            "7D", "8D", "9D", "10D", "JD", "QD", "KD"]

hand = []

while diamonds:
    choice = input("Press ENTER to pick a card or Q and enter to quit: ")

    if choice == "Q" or choice == "q":
        break

    card = random.choice(diamonds)
    diamonds.remove(card)
    hand.append(card)
    print("Your hand: ", hand)
    print("Remaining Cards: ", diamonds)
    print()

if not diamonds:
    print("There are no more cards to pick")
