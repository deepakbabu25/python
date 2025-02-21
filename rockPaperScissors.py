import random

options=("rock","paper","scissors")
player=None
computer=random.choice(options)
player=input("Enter your choice: ")
#print(f"Computer's choice: {computer}")
running=True
while running:
    while player not in options:
        
        player=input("Enter your choice")
    #print(f"Player's choice: {player}")
    #print("Computer's choice: ",computer)
    if player==computer:
        print("its a tie")
    elif player=="rock" and computer=="scissors":
        print("Player wins")
    elif player=="scissors" and computer=="paper":
        print("Player wins")
    elif player=="paper" and computer=="rock":
        print("Player wins")
    else:
        print("Computer wins")

    if not input("Do you want to play again? (y/n): ").lower()=="y":
        running=False
        
