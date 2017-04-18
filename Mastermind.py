from random import *
import random
#selects random number of four digits
name = input("Welcome to Mastermind, what is your name?")
print ("Hello there",name,"the rules to playing Mastermind are:")
print("The object of MASTERMIND (r) is to guess a secret code consisting of a series of  \
numbers. Each guest results in feedback narrowing down the possibilities of the \
code. The winner is the player who is able to solve the opponent's secret code.")



def ezGaymes():
    tries = 12
    gameEnd = False
    solution = []
    for i in range(4):
        solution.append(randint(1,6))
    print (solution)
    guessesMade = []
    while gameEnd == False:
        user_input = str(input("Enter a four-digit Number"))
        guessesMade.append(user_input)
        print (guessesMade)
        count = 0
        thisGuess = []
        for a in range(4):
            thisGuess.append(int(user_input[a]))
        for i in range(4):
            if thisGuess[i] == solution[i]:
                count = count + 1
        print ("Numbers:", count)
        if count != 4:
            tries = tries - 1
            print (tries)
    
    



difficulty = input("Choose your difficulty: easy or expert")
while (difficulty != "easy") and (difficulty != "expert"):
    print("Choose an easy or expert difficulty")
    difficulty = input()

if difficulty == "easy":
    ezGaymes()
