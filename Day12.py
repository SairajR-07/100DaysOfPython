from random import randint

Easy_level=10
Hard_level=5


def check_answer(user_guess, actual_answer,turns):
    if user_guess > actual_answer:
        print("Your guess is too high")
        return turns-1
    elif user_guess < actual_answer:
        print("Your guess is too low")
        return turns - 1
    else:
        print(f"Correct! THe answer is:{actual_answer}")

def set_difficulty():
    level=input("Choose the difficulty level. Type 'easy' or 'hard' ")
    if level == "easy":
        return Easy_level
    else:
        return Hard_level

def game():
    print("Welcome To The Number Guessing Game!!!")
    print("Im thinking of a number between 1 o 100.")
    answer=randint(1,100)

    turns=set_difficulty()
    guess=0
    while guess!=answer:
        print(f"You have {turns} guesses left.")
        guess=int(input("Guess a number: "))

        turns=check_answer(guess,answer,turns)
        # check_answer(guess, answer)

game()