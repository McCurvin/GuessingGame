#Mc Curvin Royeras
import random


def guessnumber():
    name = input("Name: ")
    bet = int(input("Bet (divisible by 10): "))
    max = int(input("Max number (more than 4): "))
    prize = 10 * max
    g = random.randint(1, max)
    numGuess = 0

    print(f"Well, {name}, guess 1 to {max} to win {prize}.")
    while True:
        guess = int(input("Take a guess: "))
        numGuess += 1

        if guess == g:
            print(f"Good job, {name}! Guessed in {numGuess} guesses! You won {prize}.")
            break
        elif numGuess == 3:
            print(f"Sorry, {name}! You lost.")
            break
        else:
            print("Your guess is too high." if guess > g else "Your guess is too low.")

if __name__ == "__main__":
    guessnumber()

