import random
import time

#creating a list of possible choices for the players
options= ["rock", "paper","scissor"]

#saving the players name
playerName= input("Enter players name: ")
print("")

#initializing both players' scores
playerScore=0
opponentScore=0

#creating variables to monitor the number of rounds played(r) and the number of iterations(i) 
i=3
r=1

#iterating my while loop until i=0
while i>0:
    
    #game design I guess? (^_^)
    print(f"..........................................round {r}......................................")

    time.sleep(1)
    print(options[0])
    time.sleep(1)
    print(options[1])
    time.sleep(1)
    print(options[2])
    time.sleep(1)
    print("shoot!!!!!!")
    time.sleep(1)

    #prompting the user to pick an option and making sure a bad input doesn't break the game
    print("")
    playerChoice= input("pick one: ")
    playerChoice=playerChoice.lower()
    while True:
        if playerChoice in options:
            break
        else:
            playerChoice= input("choose amongst rock, paper or scissor: ")
            if playerChoice.lower() in options:
                playerChoice=playerChoice.lower()
                break
            
    #using a method from the random module to generate a random opponent
    time.sleep(1)
    print("")
    opponentChoice= random.choice(options)
    print(f"your opponent's choice:  {opponentChoice}")
    print("")

    #designing the game algorithm (making sure a tie adds an additional round)
    while True:
        if playerChoice==opponentChoice:
            print("replay round!^_^")
            i+=1
            break
        
        elif playerChoice=="rock":
            if opponentChoice=="paper":
                opponentScore+=1
                print(f"opponent won!")
                break
            if opponentChoice=="scissor":
                playerScore+=1
                print(f"{playerName} won!")
                break
        
        elif playerChoice=="paper":
            if opponentChoice=="rock":
                playerScore+=1
                print(f"{playerName} won!")
                break
            if opponentChoice=="scissor":
                opponentScore+=1
                print(f"opponent won!")
                break

        elif playerChoice=="scissor":
            if opponentChoice=="rock":
                opponentScore+=1
                print(f"opponent won!")
                break
            if opponentChoice=="paper":
                playerScore+=1
                print(f"{playerName} won!")
                break


    print(f"{playerName}'s score: {playerScore} / opponent's score:{opponentScore}")
    i-=1
    r+=1
    if opponentScore==2:
        break
    if playerScore==2:
        break


#Displaying the winner, YAY!!
print("")
print(f"THE WINNER IS: {playerName if playerScore>opponentScore else "opponent"}")