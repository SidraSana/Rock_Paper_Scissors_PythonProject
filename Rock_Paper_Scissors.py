import random
# Initial scores of user and computer are 0
user_score = 0
computer_score = 0

# options[0] = Rock, options[1] = Paper, options[2] = Scissors,
options = ["rock", "paper", "scissors"]


while True:
    user = input(" Enter Rock/Paper/Scissors or Q to quit: ").lower()
    if user == "q":
        print("You Quit")
        break

    if user not in ["rock", "paper", "scissors"]:
        print("Invalid Input")
        continue

    r = random.randint(0,2)
    computer = options[r]
    print("Computer's turn: ", computer + ".")

    if user == "rock" and computer == "scissors":
        print("You Win!")
        user_score += 1

    elif user == "paper" and computer == "rock":
        print("You Win!")
        user_score += 1

    elif user == "scissors" and computer == "paper":
        print("You Win!")
        user_score += 1

    elif user == "scissors" and computer == "scissors":
        print("Match Draw!")


    elif user == "rock" and computer == "rock":
        print("Match Draw!")

    elif user == "paper" and computer == "paper":
        print("Match Draw!")

    else:
        print("You Lost!")
        computer_score += 1

print("You won ", user_score, " times")
print("Computer won ", computer_score, " times")
print("Goodbye!")





