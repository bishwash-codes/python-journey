import random

options = ("rock", "paper", "scissors")

cont = True

while cont:
    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter your choice : Rock , Paper , Scissors ; ").lower()

    print(f"player : {player}")
    print(f"computer : {computer}")

    if player == computer:
        print("its a tie")
    elif player == "rock" and computer == "scissors":
        print("Player wins")
    elif player == "paper" and computer == "rock":
        print("Player wins")
    elif player == "scissors" and computer == "paper":
        print("Player wins")
    else:
        print("Player lose")

    continue_play = input("Play again ? (yes/no) ").lower()
    if not continue_play == "yes":
        cont = False

print("Thanks for playing.")
