# # binary
# for i in range(17):
#     print("{0:>2} in binary is {0:>08b}".format(i))
#
# # hexadecimal
# for i in range(17):
#     print("{0:>2} in hex is {0:>02x}".format(i))
#
# x = 0x20
# y = 0x0a
#
# print(x)
# print(y)
# print(x * y)
#
# print(0b01011010)
#
# for i in range(17):
#     print("{0:>2} in hex is {0:>02x}".format(i))
#
# x = 0x20
# y = 0x0a
#
# print(x)
# print(y)
# print(x * y)
#
# print(0b101010)

# When converting a decimal number to binary, you look for the highest power
# of 2 smaller than the number and put a 1 in that column. You then take the
# remainder and repeat the process with the next highest power - putting a 1
# if it goes into the remainder and a zero otherwise. Keep repeating until you
# have dealt with all powers down to 2 ** 0 (i.e., 1).
#
# Write a program that requests a number from the keyboard, then prints out
# its binary representation.
#
# Obviously you could use a format string, but that is not allowed for this
# challenge.
#
# The program should cater for numbers up to 65535; i.e. (2 ** 16) - 1
#
# Hint: you will need integer division (//), and modulo (%) to get the remainder.
# You will also need ** to raise one number to the power of another:
# For example, 2 ** 8 raises 2 to the power 8.
#
# As an optional extra, avoid printing leading zeros.
#
# Once the program is working, modify it to print Octal rather than binary.

decNumber = int(input("Enter a number to convert to binary:\n"))
binNumber = ""
finalBinNumber = ""
exNumber = decNumber // 2
modNumber = decNumber % 2

while True:
    if exNumber > 0 and modNumber == 1:
        binNumber += "1"
        modNumber = exNumber % 2
        exNumber = exNumber // 2
    elif exNumber > 0 and modNumber == 0:
        binNumber += "0"
        modNumber = exNumber % 2
        exNumber = exNumber // 2
    elif exNumber == 0 and modNumber == 1:
        binNumber += "1"
        modNumber = exNumber % 2
        exNumber = exNumber // 2
    else:
        if binNumber == "":
            finalBinNumber += "0"
        for i in binNumber[::-1]:
            finalBinNumber += i
        break

print(finalBinNumber)
# ================== or
powers = []
x = int(input("Please enter a number:\n"))
isDivisible = x
maxPower = 0
binOrOct = 8
while isDivisible != 0:
    isDivisible //= binOrOct
    maxPower += 1

for power in range(maxPower, -1, -1):
    powers.append(binOrOct ** power)

printing = False

for power in powers:
    bit = x // power
    if bit != 0 or power == 1:
        printing = True
    if printing:
        print(x // power, end = '')
    x %= power
