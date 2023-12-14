import random

def determine_winner(user_input, computer_pick):
    if user_input == computer_pick:
        return "It's a tie!"
    elif (user_input == "rock" and computer_pick == "scissors") or \
         (user_input == "paper" and computer_pick == "rock") or \
         (user_input == "scissors" and computer_pick == "paper"):
        return "You won!"
    else:
        return "You lost!"

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        print("Invalid input. Please type Rock, Paper, Scissors, or Q to quit.")
        continue

    random_number = random.randint(0, 2)
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    result = determine_winner(user_input, computer_pick)
    print(result)

    if result == "You won!":
        user_wins += 1
    elif result == "You lost!":
        computer_wins += 1

print("You won", user_wins, "times.")
print("The computer won", computer_wins, "times.")
print("Goodbye!")