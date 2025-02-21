# January 24th, 2025

#Boys Latin has hired you to develop a grade checker program for students. 
#Your program should be able to do the following; allow a student to enter a numerical grade, 
#then return the appropriate letter grade. For example; if a student enters the number 80, the program should give back the letter grade "B". 
#Your program should then repeat by asking the user to enter another numerical grade. 
#Each time a user enters another numerical grade, it should perform some calculation to average out the grades and show the new letter grade, 
#For example: if the user enters the number 70, and the 100, they're average should be an 85, which is a B.

#1. In a complete sentence, what is the problem asking you to do ?
#The problem is asking for me to make a program that allows a stusent to inpoout their grade numerous times, then give the average grade.

#2. Were there any parts of the question that don't make sense, if so write them down in complete sentences.
# This part of the promt doesnt necessarily make sense, though im un able to understand how I would print the average grade.

#3. Please write down the keywords and phrases that will help you solve this problem ?
#   1. enter a number.    2. repeat.    3. average.    4. calculations.    5. return appropiate lette grade(output).

#4. Does the problem provide you with any input data? Does it tell you what type of data your program needs to take in ?
# The program is asking the user to inoput a number numerous times, in which the program will calculate the average amongst those grade.

#5. Does the problem provide you with desired output data? Does it tell you that your program needs to give somthing back to the user ?
# The proogram will produce the avergage letter grade.

#6. Using Pseudocode (fake code), write down Step by step how you think you can solve this problem. Remember, this does not have to be code.
# first i would give the program a name.
# then i would insert various inputs, for the user to input their grade.
# then i would use arithmatic coding for the computer to read, so it gives the avergae letter grade.


#You are working on a game concept with several other engineers and you need to provide them with a simple proof of concept. 
#For now, you have suggested that your game work on a RPS (rock, paper, scissors) loop. When a user plays, rock, paper, or scissors, 
#the computer will randomly select one of the 3 options as well. Based on the results of a match, Your program should conditionally determine who won, 
#loss, or if it was a draw based on the values. The game should only allow the player to play 3 for 3 turns, and inform the player if the won or lost that match at the end 
#(this RPS game is a best of 2 out of 3 format.)

#1. In a complete sentence, what is the problem asking you to do ?
# The question is asking me to code a program that allows a user, and a computer to input data, in order to decipher who won that game.

#2. Where there any parts of the question that don't make sense, if so write them down in complete sentences.
# There were no parts that i didnt understand.

#3. Please write down the keywords and phrases that will help you solve this problem ?
#   1. loop     2. rock, paper, scissor     3. 2 out of 3     4. values

#4. Does the problem provide you with any input data? Does it tell you what type of data your program needs to take in ?
# The problem provides various input datas for the user, in which must be rock, paper, or scissor.

#5. Does the problem provide you with desired output data? Does it tell you that your program needs to give somthing back to the user ?
# The desired output for this program is who won the game, and runs the program again 2 or more times, to decide whos won the game.

#6. Using Pseudocode (fake code), write down Step by step how you think you can solve this problem. Remember, this does not have to be code.
# first i would name the function
# then i would give each variable a value (rock, paper, and scissors).
# then I would insert input functions for the user, and the compuer.
# Then I would create a loop to run 3 times.
# lastley i would make the program decipher who won or not based on the 3 games that were played.


import random

def rpsGame():
    rpsValues = ['rock', 'paper', 'scissor']
    turn = 0
    while turn >3:
        userSelects = input ('Please select an option 0=rock, 1=paper, 2=scissor')
        programSelects= rpsValues(random.randrange(0,2))
        if userSelects==0 and programSelects==0:
            print('This is a draw')
        elif userSelects==0 and programSelects==1
            print('Program has won')
        else:
            print('Something went wrong, check your code.')

rpsGame()