import random

secret_num = random.randint(1,10)

print(secret_num)

guess_num = int(input("Guess number (1-10): "))

if secret_num == guess_num:
    print("You guessed it right!")
elif guess_num < secret_num:
    if guess_num >= 1:
        print("Too low")
    else:
        print("Your input is out of range (1 - 10)")
elif guess_num > secret_num: 
    if guess_num <= 10:
        print("Too high")        
    else:
        print("Your input is out of range (1 - 10)")



print("This is outside and after the IF block")