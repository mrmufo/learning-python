# name = input("Enter your name: ")
# age = int(input("How old are you, {0}? ".format(name)))
# print(age)
#
# if age >= 18:
#     print("You are old enough to smoke.")
# if 0 <= age < 17:
#     print("Please come back in {0} years.".format(18 - age))
# if age == 17:
#     print("Please come back in 1 year.")
# else:
#     print("Incorrect data. Age can not be less than 1.")
#
print("Please guess a number between 1 and 10: ")
guess = int(input())

if guess != 5:
    if guess < 5:
        print("Please, guess higher.")
    else:
        print("Please, guess lower.")
    guess = int(input())
    if guess == 5:
        print("Well done, you guessed it.")
    else:
        print("Sorry, you have not guessed correctly.")
else:
    print("Well done, you guessed it in first try!")
