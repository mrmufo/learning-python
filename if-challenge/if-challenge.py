name = input("Enter your name: ")
age = int(input("Enter your age: "))

if 18 <= age <= 31:
    print("Great {0}! We will have priceless adventure during the holiday. ".format(name))
elif 0 < age < 18:
    print("Sorry {0}, you are too young. Come back in {1} years. ".format(name, (18 - age)))
elif age > 31:
    print("Sorry {0}, you are too old. ".format(name))
else:
    print("Incorrect age. ")

