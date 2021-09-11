import random


def guess_random_number(tries, start, stop):
    rand_num = random.randint(start, stop + 1)
    while tries > 0:
        print("Number of tries left: ", + tries)
        while True:
            guess = int(input("Guess a number between " + str(start) + " and " + str(stop) + ": "))
            if guess.isnumeric() and guess >= start and guess <= stop:
                break

        if guess == rand_num:
            print("You guessed the correct number!")
            return
        elif guess < rand_num:
            print("Guess higher!")
        elif guess > rand_num:
            print("Guess lower!")
        tries -= 1

    print("You have failed to guess the number: " + str(rand_num))


def guess_random_num_linear(tries, start, stop):
    rand_num = random.randint(start, stop)
    print("The number for the program to guess is: ", + rand_num)

    for guess in range(start, stop+1, 1):
        print("Number of tries left: ", + tries)
        print("The program is guessing... ", + guess)
        if guess == rand_num:
            print("The program has guessed the correct number!")
            return
        tries -= 1
        if tries == 0:
            print("The program has failed to guess the correct number.")
            return


def guess_random_num_binary(tries, start, stop):
    rand_num = random.randint(start, stop)
    print("Random number to find: ", + rand_num)

    while start <= stop:
        guess = (start + stop) // 2

        if guess == rand_num:
            print("Found it! ", + guess)
            return
        if guess > rand_num:
            stop = guess - 1
            print("Guessing lower!", +guess)
        else:
            start = guess + 1
            print("Guessing higher!", +guess)

        tries -= 1
        if tries == 0:
            print("Your program failed to find the number.")
            return


#guess_random_number(5, 0, 10)
#guess_random_num_linear(5, 0, 10)
#guess_random_num_binary(5, 0, 100)
