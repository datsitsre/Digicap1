"""
File: guessmynumber.py
----------------------
This program checks if a user's guess of a number matches that guessed by the computer
"""

# print(random.randint(30, 50))
import random
#
#
check = True #set a variable to true for the while loop
# get the random  number
rand_number = random.randint(1,99)
while check: # check if varible is true

    user_input = int(input("Enter a guess: ")) #get user inputs

    if user_input == rand_number:   #condition of if user input is less than randon number
        print("Your guess is right : ", user_input)  # if the user input is correct print you are right
        check = False #change check variable to false to exit the loop
    elif user_input < rand_number:  #user  input is greater than randon number
        print(user_input , " is low") #print user input is high
    else:
        print(user_input , " is high" ) #print the statement user input is wrong




# ********************************** YOUR CODE GOES BELOW HERE *********************************************************
