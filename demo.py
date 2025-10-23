import random

secret_number = random.randint(1,10)

print(secret_number)
#Ask user input
guess_number = int(input("Guess number (1-10): "))

#Check if user input == secret number
if guess_number == secret_number:
    print("You guessed it right!")
elif guess_number <= secret_number:
    if guess_number>=1:
        print("Too low")
elif guess_number >= secret_number and guess_number<=10:
    print("Too high")
else:
    print("Invalid input.")

print("This is outside of if")