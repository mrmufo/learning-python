# Modify the program below to use a while loop to
# allow as many guesses as necessary.
#
# The program should let the player know whether to
# guess higher or lower, and should print a message
# when the guess is correct. A correct guess will
# terminate the program.
#
# As an optional extra, allow the player to quit by entering
# 0 (zero) for their guess.
import random

attempts = 5
highest = 10
answer = random.randint(1, highest)

print("Please guess a number between 1 and {}: ".format(highest))
guess = int(input())
while attempts != 0:
    if guess != answer:
        if guess < answer:
            print("Please guess higher:")
        else:
            print("Please guess lower: ")
        guess = int(input())
        attempts -= 1

        if guess == answer:
            print("Well done, you guessed it. ")
            break
        elif guess == 0:
            print("You gave up. Shame on you!")
            break
    else:
        print("You got it first time! ")
        break
else:
    print("Sorry, you have run out of guess attempts. ")
