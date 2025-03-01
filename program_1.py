# Author: Lucia Floan
# Date: Feb 28, 2025
# Title: Random Dice

# Program #1: Random Dice
# Write a "randDice" function (with no input) that randomly chooses two numbers between 1 and 6 (inclusive) and then adds them (this is to simulate the rolling of 2 dice).  
# The dice sum will be the output of this function.

#Pseudocode:

import random 

def randDice():
    # Write your logic to generate 2 numbers between 1 and 6 here
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    # Sum 2 numbers
    return dice1 + dice2 # return sum to calling function
#########
# Then write a mainline that calls the "randDice" function 100 times in a for loop.  
# The mainline then prints the average of the 100 rolls, rounded to the nearest 0.01.
total_sum = 0

for _ in range(100):
    total_sum += randDice()
average = round(total_sum / 100, 2)
print('The average of 100 rolls:', average)
