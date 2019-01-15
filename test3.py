import random

print("Dice Game: try to roll a bigger number than the computer! Good luck!")

print("Type 'go' to roll")
diceroll = input()
if diceroll == 'go':
    myNumber = random.randint(1,6)
    pcNumber = random.randint(1,6)
    print("You rolled " + str(myNumber))
    print("He rolled " + str(pcNumber))
    if myNumber < pcNumber:
        print("you lose!")
    if pcNumber < myNumber:
        print("You win!")