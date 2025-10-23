import random

secret_num = random.randint(1, 10)

guess_num = input("Guess num (1-10): ")

if secret_num == guess_num:
    print("You guessed it right!")
elif 