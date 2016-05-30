# First Solution
import random

number = random.randrange(0, 19)
guess = int(input("Enter an integer between 1 and 20: "))

while guess != number:
    if guess == number:
        print("You guessed correctly!")
        continue
    elif guess < number:
        print("Too low yo")
        continue
    elif guess > number:
        print("Too high guy")
        continue

# Second Solution
