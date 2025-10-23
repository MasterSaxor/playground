import random

secret_num = random.randint(1, 10)

print(secret_num)

guess_num = int(input("Guess number (1-10): "))

#guess_num = int(guess_num)

if guess_num == secret_num:
    print("You guessed it right!")
elif guess_num < secret_num 
    if guess_num >= 1 and guess_num != letters:
    print("Too low")
elif guess_num > secret_num and guess_num <= 10:
    print("Too high")
else:
    print("Guess number should be from 1 to 10 only.")

print("The program will continue here.")
