# for i in range(0,20):
#     print("i is now {0}".format(i))
#
# number = "9,922,543,263,469,003,216"
# cleanedNumber = ''
#
# for i in range(0, len(number)):
#     if(number[i] in '0123456789'):
#         cleanedNumber = cleanedNumber + number[i]
# print(cleanedNumber)
# newNumber = int(cleanedNumber)
# print("The number is {}. ".format(newNumber))
#
number = "9,922,543,263,469,003,216"
cleanedNumber = ''

for char in number:
    if char in "0123456789":
        cleanedNumber = cleanedNumber + char

newNumber = int(cleanedNumber)
print("The number is {}. ".format(newNumber))

for state in ["not pinin'", "no more", "a stiff", "bereft of lift"]:
    print("This parrot is " + state)

for i in range(0, 100, 5):
    print("i is {}".format(i))

for i in range(1, 13):
    for j in range (1, 13):
        print("{1:2.0f} times {0} is {2:3.0f}".format(i, j, i*j), end = '\t')
    print('')
