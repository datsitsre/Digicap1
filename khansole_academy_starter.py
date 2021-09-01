"""
File: khansole_academy.py
-------------------------
Khansole Academy is a program that teaches users how to add by asking users to input answers for the addition of two
randomly generating integers between 10 and 99 inclusive. The program returns feedback based on the User's answers.

"""
#import the random module
import random

# use code below  to generate a random integer between 30 and 50 for example
#counter for the correct answer
count = 0

#loop that meets the 3 correct answers
while count < 3:
    addend1 = random.randint(1,99) #get the first number
    addend2 = random.randint(1,99) #get the second number
    sum = addend1 + addend2   #add the two numbers
    print("What is " , addend1 ,"+" , addend2, ":  ") #print out the question for the user to ask
    user_input = int(input("Answer: "))   #Get user input
    if sum == user_input:     #Check if the user answer is same as the addition
        print("Your answer is correct ")  # print your correct answer
        count +=1       #increase the count for the correct answer
        print("You have answered ", count)  #print the number of  times the user has answer the question
    else:    #Otherwise
        print("Answer is incorrect") #print the answer is incorrect
print("Congratulations, You have masted the program")  #print a final message of congratulations
# ********************************** YOUR CODE GOES BELOW HERE *********************************************************
