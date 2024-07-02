#Explain rules
print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")

import random
number = random.randint(1,10)

isGuessRight = False

#If the user has not guessed the correct answer, enter the loop.
while isGuessRight != True:
    #Ask the user for a guess.
    guess = input("Guess a number between 1 and 10: ")
   #Is the guess the correct number?
    if int(guess) == number:
        #If the correct guess, tell the user it was the correct guess and exit the loop.
        print("You guessed {}. That is correct! You win!".format(guess))
        isGuessRight = True
        #If the wrong guess, tell the user it was the wrong guess and continue the loop
    else:
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))
        