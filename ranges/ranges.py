# # myList = list(range(10))
# # print(myList)
# #
# # even = list(range(0, 10, 2))
# # odd = list(range(1, 10, 2))
# #
# # print(even)
# # print(odd)
# #
# # myString = "abcdefghijklmnoprstuvwxyz"
# # print(myString.index('e'))
# # print(myString[4])
# #
# # smallDecimals = range(0, 10)
# # print(smallDecimals)
# # print(smallDecimals.index(3))
# #
# # odd = range(1, 10000, 2)
# # print(odd)
# #
# # print(odd[985])
# #
# # sevens = range(7, 1000000, 7)
# # x = int(input("Please enter a positive number less than one million: "))
# # if x in sevens:
# #     print("{} is divisible by seven.".format(x))
# #
# # print(smallDecimals)
# # myRange = smallDecimals[::2]
# # print(myRange)
# # print(myRange)
# # print(myRange.index(8))
# #
# # decimals = range(0, 100)
# # print(decimals)
# #
# # myRange = decimals[3:40:3]
# # print(myRange)
# #
# # for i in myRange:
# #     print(i)
# #
# # print('=' * 40)
# #
# # for i in range(3, 40, 3):
# #     print(i)
# #
# # print(myRange == range(3, 40, 3))
# #
# decimals = range(0, 100)
# myRange = decimals[3:40:3]
# print(myRange == range(3, 40, 3))
# print(range(0, 5, 2) == range(0, 6, 2))
# print(list(range(0, 5, 2)))
# print(list(range(0, 6, 2)))
#
# r = range(0, 100)
# print(r)
#
# for i in r[::-2]:
#     print(i)
# print('=' * 50)
# for i in range(99, 0, -2):
#     print(i)
# print('=' * 50)
# print(range(0, 100)[::-2] == range(99, 0, -2))
#
# for i in range(0, 100, -2):
#     print(i)
#
# backString = ".egaugnal lufrewop yrev a si nohtyP"
# print(backString[::-1])
#
# r = range(0, 10)
# for i in r[::-1]:
#     print(i)
#
# Experiment with different ranges and slices to get a feel for how they work.
# Remember that you can print the range as well as iterating through it to print
# its values, to check that your ranges are what you expected.
# You may also want to include things like.
#
# o = range(0, 100, 4)
# q = range(100, 0, -2)
# print(q)
# print(o)
# p = o[::5]
# print(p)
# for i in p:
#     print(i)
# for i in q:
#     print(i)

# and see if you can work out what will be printed before running the program. If you are unsure, use a
# for loop to print out the values of o to see why p returns what it does.
alphabet = " abcdefghijklmnopqrstuvwABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabetBackString = alphabet[::-1]
indexedMessage = []
decIndexedMessage = []
decryptedMessage = ""
encryptedMessage = ""
menu = 1
while menu != '0':
    menu = input("Press 1 to encrypt\n"
                 "Press 2 to decrypt\n"
                 "Press 0 to exit")
    if menu == '1':
        rawMessage = input("Enter your message to encrypt: ")

        for i in rawMessage:
            indexedMessage.append(alphabet.index(i))

        for i in indexedMessage:
            print(i)

        for i in indexedMessage:
            encryptedMessage += alphabetBackString[i]
        print(encryptedMessage)
    elif menu == '2':
        rawMessage = input("Enter your encrypted message: ")

        for i in rawMessage:
            decIndexedMessage.append(alphabetBackString.index(i))

        for i in range(0, len(decIndexedMessage)):
            decryptedMessage += alphabet[decIndexedMessage[i]]
        print(decryptedMessage)
    elif menu == '0':
        print("Exit")
        break
else:
    print("Wrong input, try again.")
