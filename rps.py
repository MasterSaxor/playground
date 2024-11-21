from random import randint


computer = ""
player_wins = 0
computer_wins = 0
winning_score = 3

while player_wins < winning_score and computer_wins < winning_score:

    player = input("Enter your choice: ").lower().strip()

    print(f"Player Score: {player_wins} Computer Score: {computer_wins}")

    if player == "quit" or player == "q":
        break

    # Ask the user for input (rock, paper, scissors)r 
    random = random.randint(0,2)  
    if  random == 0:
        computer = "rock"
    elif random == 1:
        computer = "paper"
    elif random == 2:
        computer = "scissors"

    print(f"Computer plays {computer}")

    # Emulate the mechanics of bato-bato-pik
    if player == computer:
        print("It's a tie!")
    elif player == "rock":
        if computer == "paper":
            print("Computer wins!")
            computer_wins += 1
        elif computer == "scissors":
            print("Player wins!")
            player_wins += 1
    elif player == "paper":
        if computer == "scissors":
            print("Computer wins!")
            computer_wins += 1
        elif computer == "rock":
            print("Player wins!")
            player_wins += 1
    elif player == "scissors":
        if computer == "rock":
            print("Computer wins!")
            computer_wins += 1
        elif computer == "paper":
            print("Player wins!")
            player_wins += 1

# Display the winner
print(f"Final Score...   Player Score: {player_wins} Computer Score: {computer_wins}")

if player_wins > computer_wins:
    print("You beat the AI. Great!!!")
elif player_wins == computer_wins:
    print("Its a tie!")
else:
    print("You lose to the AI!")

