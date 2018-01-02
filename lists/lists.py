# # ipAddress = input("Please enter and IP address: ")
# # print(ipAddress.count("."))
# #
# parrot_list = ["non pinin'", "no more", "a stiff", "bereft of love"]
#
# parrot_list.append("A Norwegian Blue")
#
# for state in parrot_list:
#     print("This parrot is " + state)
#
# even = [2, 4, 6, 8]
# odd = [1, 3, 5, 7, 9]
# numbers = even + odd
# numbers.sort()
# print(numbers)
#
# numbersInOrder = sorted(numbers)
#
# if numbers == numbersInOrder:
#     print("The lists are equal.")
# else:
#     print("The lists are not equal.")
#
# list_1 = []
# list_2 = list()
#
# print("List 1: {} ".format(list_1))
# print("List 2: {} ".format(list_2))
#
# if list_1 == list_2:
#     print("The lists are equal.")
#
# print(list("The lists are equal."))
#
# even = [2, 4, 6, 8]
#
# #  another_even = even -> even and another_even refer to the same list
# #  another_even = list(even)
# another_even = sorted(even, reverse=True)
# print(another_even is even)
# #  another_even.sort(reverse=True)
# print(even)
# print(another_even)
#
# even = [2, 4, 6, 8]
# odd = [1, 3, 5, 7, 9]
#
# numbers = [even, odd]
#
# for numbers_set in numbers:
#     print(numbers_set)
#
#     for value in numbers_set:
#         print(value)
#
menu = []
menu.append(["egg", "spam", "bacon"])
menu.append(["egg", "sausage", "bacon"])
menu.append(["egg", "spam"])
menu.append(["egg", "bacon", "spam"])
menu.append(["egg", "bacon", "sausage", "spam"])
menu.append(["spam", "bacon", "sausage", "spam"])
menu.append(["spam", "egg", "spam", "spam", "bacon", "spam"])
menu.append(["spam", "egg", "sausage", "spam"])

#  print(menu)

for meal in menu:
    if not "spam" in meal:
        print(meal)
