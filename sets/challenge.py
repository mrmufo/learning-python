# vowels = ("a", "e", "i", "o", "u", "y")
# alphabet = "abcdefgijklmnopqrstuvw"
# textInput = input("Enter text: ")
# text = textInput  # set(textInput)
# print(text)
# print(vowels)
# for letter in text:
#     if letter in vowels:
#         continue
#     else:
#         print(letter + ", ")

sampleText = input("Enter text:")
print(sampleText)
vowels = frozenset("aeiou")
finalSet = set(sampleText).difference(vowels)
print(finalSet)

finalList = sorted(finalSet)
print(finalList)