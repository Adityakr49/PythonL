import random

while True:
    choices=["rock","paper","scissors"]
    computer = random.choice(choices)
    player=None

    while player not in choices:
        player=input("rock, paper, or scissors?: ").lower()

    def printing():
        print("computer: ", computer)
        print("player: ", player)

    if player==computer:
        printing()
        print("Tie")
    elif player=="rock":
        if computer=="paper":
            printing()
            print("You Lose!")
        elif computer=="scissors":
            printing()
            print("You win!")
    elif player=="paper":
        if computer=="scissors":
            printing()
            print("You lose!")
        elif computer=="rock":
            printing()
            print("You win!")
    else:
        if computer=="rock":
            printing()
            print("You lose!")
        elif computer=="paper":
            printing()
            print("You win!")
    play_again=input("Play again? (yes/no): ").lower()
    if play_again!="yes":
        break
print("bye")