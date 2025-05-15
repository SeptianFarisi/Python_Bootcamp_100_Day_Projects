import random
from art import logo

def gameplay():
    number = random.randint(1, 100)
    hp = 0
    game = False
    print(logo)
    print("Welcome to the Togel Game!")
    print("I'm thinking of a number between 1 and 100")
    guess_hp = input("Choose a difficulty? 'easy' or 'hard'\n").lower()
    if guess_hp == "easy":
        hp += 10
    elif guess_hp == "hard":
        hp += 5
    else:
        print("Please choose a difficulty")

    while not game:
        if hp < 1:
            print(f"You've run out of guesses. guess number is {number}")
            game = True
        else:
            print(f"You have {hp} attempts ramaining to guess the number.")
            guess = int(input("Make a guess? "))
            if guess < number:
                hp -= 1
                print("Too low.")
                print("Guess again.")
            elif guess > number:
                hp -= 1
                print("Too high.\nGuess again.")
            elif guess == number:
                print(f"You got it the answer was {number}")
                game = True

while input("You wanna play Togel :v? type 'y' to play or 'n' to exit\n").lower() == "y":
    gameplay()