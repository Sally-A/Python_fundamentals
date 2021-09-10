# Blackjack ---  python object oriented programming.
# Future options:  1. add betting.  2. Multi Player 3. add user name 4. add multiple decks
# ==========================================================================================================

# import dependencies
import random
import os
import sys

# class for card values and suits


class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        return

    def __repr__(self):
        # return f"{self.value} of {self.suit}"
        return f"{self.value} {self.suit}"


# class for building the deck (inheriting from Card class), shuffling the deck and drawing a card
class Deck:
    def __init__(self):
        #suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
        # characters for suits
        suits_values = {"Spades": "\u2664", "Hearts": "\u2661",
                        "Clubs": "\u2667", "Diamonds": "\u2662"}
        values = ["2", "3", "4", "5", "6", "7",
                  "8", "9", "10", "J", "Q", "K", "A"]
        self.cards = []

        # create deck of cards
        for suit in suits_values.values():
            for value in values:
                card = Card(value, suit)
                self.cards.append(str(card))
        return

    def shuffle(self):
        random.shuffle(self.cards)
        return

    def draw(self):
        return self.cards.pop()

    def __repr__(self):
        return f"{self.cards}"


# class for player hand and add a card & score
class Player:
    def __init__(self):
        self.hand = []
        self.sum = 0
        self.non_aces = ""
        self.aces = ""
        return

    def add_card(self, deck):
        self.hand.append(deck.draw())
        return

    def score(self):
        self.sum = 0
        self.non_aces = [card[:2] for card in self.hand if card[:1] != "A"]
        self.aces = [card[:2] for card in self.hand if card[:1] == "A"]

        for card in self.non_aces:
            card = card.strip()
            if card in "JQK":
                self.sum += 10
            else:
                self.sum += int(card)

        for card in self.aces:
            if self.sum <= 10:
                self.sum += 11
            else:
                self.sum += 1
        return self.sum

    def __repr__(self):
        return f'Player Cards: [{"][".join(self.hand)}] -----> {self.sum}'


# class for dealer hand and dealer total score (inheriting from Player class) & output string
class Dealer(Player):

    def __repr__(self):
        return f'Dealer Cards: [{"][".join(self.hand)}] -----> {self.sum}'


# class for playing.  hit and stand
class Play:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.player = Player()
        self.dealer = Dealer()

        self.first_hand = True
        self.standing = False
        self.p_score = 0
        self.d_score = 0
        self.choice = ""
        return

    def play_blackjack(self):
        # adding first hand
        self.player.add_card(self.deck)
        self.dealer.add_card(self.deck)
        self.player.add_card(self.deck)
        self.dealer.add_card(self.deck)

        while True:
            # for windows 'cls' for mac & linux 'clear' -- import os,
            os.system("cls" if os.name == "nt" else "clear")

            self.p_score = self.player.score()
            self.d_score = self.dealer.score()

            print("---------------------------------")
            print("***         BlackJack!        ***")
            print("---------------------------------")
            print("")
            if self.standing:
                print(self.dealer)
            else:
                print(f"Dealer Cards: [{self.dealer.hand[0]}][?]")

            print(self.player)
            print("")

            if self.standing:
                if self.d_score > 21:
                    print("Dealer busted, you win!")
                elif self.p_score == self.d_score:
                    print("Tie!! ")
                elif self.p_score > self.d_score:
                    print("You win!")
                else:
                    print("You lose!!")
                break

            if self.first_hand and self.p_score == 21:
                print("BlackJack! You win! Game Over!")
                break

            self.first_hand = False

            if self.p_score > 21:
                print("You busted!")
                break

            print("What would you like to do?")
            print(" [1] Hit")
            print(" [2] Stand")
            print(" [3] Quit")
            print("")

            self.choice = input("Enter Your choice: ")
            print("")
            if self.choice == "1" or self.choice[0].lower() == "h":
                self.hit()
            elif self.choice == "2" or self.choice[0].lower() == "s":
                self.stand()
            elif self.choice == "3" or self.choice[0].lower() == "q":
                sys.exit()          # import sys to use this
        return

    def hit(self):
        self.player.add_card(self.deck)
        return

    def stand(self):
        self.standing = True
        while self.dealer.score() <= 16:
            self.dealer.add_card(self.deck)
        return


# main
if __name__ == "__main__":
    play = Play()
    play.play_blackjack()

play_again = "Y"

while play_again:

    play_again = input("\nDo you want to play again? Enter Y/N: ")

    if play_again[0].lower() == "y":
        play = Play()
        play.play_blackjack()
    elif play_again[0].lower() == "n":
        print("\nGood Bye!")
        break
    else:
        print("\nYou must enter Y/N. Please try again!")
        pass
