# ipAddress = input("Please enter and IP address: ")
# print(ipAddress.count("."))
#
parrot_list = ["non pinin'", "no more", "a stiff", "bereft of love"]

parrot_list.append("A Norwegian Blue")

for state in parrot_list:
    print("This parrot is " + state)

even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]
numbers = even + odd
numbers.sort()
print(numbers)

numbersInOrder = sorted(numbers)

if numbers == numbersInOrder:
    print("The lists are equal.")
else:
    print("The lists are not equal.")
