import random

choices = ["paper", "rock","scissor"]

Player1Pick = input('''
Select A Number :
0 - paper
1 - rock
2 - scissor

Player 1 Choice -> ''')

def cpuChoice():
    return random.choice(choices)

def battle(p1,cpu):
    cpuChoice = cpu
    player1Choice = choices[int(p1)]


    if(player1Choice == "paper" and cpuChoice == "rock"):
        print("Paper covers Rock! \nYOU WIN!!")

    if(player1Choice == "scissor" and cpuChoice == "paper"):
        print("Scissors cut Paper! \nYOU WIN!!")

    if(player1Choice == "rock" and cpuChoice == "scissor"):
        print("Rock breaks Scissors! \nYOU WIN!!")

    if(cpuChoice == "paper" and player1Choice == "rock"):
        print("Paper covers Rock! \nYOU LOSE!!")

    if(cpuChoice == "scissor" and player1Choice == "paper"):
        print("Scissors cut Paper! \nYOU LOSE!!")

    if(cpuChoice == "rock" and player1Choice == "scissor"):
        print("Rock breaks Scissors! \nYOU LOSE!!")

    if(player1Choice == cpuChoice):
        print("Draw!!")

try:
    battle(int(Player1Pick), cpuChoice())
except:
    print("Please select 0 -paper, 1 - rock, or 2 - dscissor")