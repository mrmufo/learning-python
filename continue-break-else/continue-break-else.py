# shopping_list = ["milk", "pasta", "eggs", "spam", "rice"]
# for item in shopping_list:
#     if item == 'spam':
#         print("I am ignoring " + item)
#         continue
#
#     print("Buy " + item)
#

meal = ["egg", "bacon", "spam", "sausages"]
nastyFoodItem = ''

for item in meal:
    if item == 'spam':
        nastyFoodItem = item
        break
else:
    print("I'll have a plate of that, then, please")

if nastyFoodItem:
    print("Can't I have anything without spam in it")
