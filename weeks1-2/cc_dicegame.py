import random

high_score = 0


def dice_game():
    global high_score
    while True:
        score = 0

        # menu
        print()
        print("Current High Score: ", high_score)
        print("1) Roll Dice")
        print("2) Leave Game")
        selected = input("Enter your choice: ")
        print()

        if selected == "1":
            for i in range(2):
                roll = random.randint(1, 6)
                print("Die", i+1, "You roll a... ", roll)
                score += roll

            print("\nYou have rolled a total of: ", score)
            if(score > high_score):
                high_score = score
                print("\nNew high score")
        elif selected == "2":
            print("\nGoodbye")
            quit()
        else:
            print("Invalid Choice - Try again\n")


dice_game()
