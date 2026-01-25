import random

number = random.randint(1, 10)
guess = 0

while guess != number:
    guess = int(input("Guess the number (1-10): "))

    if guess < number:
        print("Too low")
    elif guess > number:
        print("Too high")
    else:
        print("Correct")