import shelve

books = shelve.open("book")
books["recipes"] = {"blt": ["bacon", "lettuce", "bread"],
                    "beans_on_toast": ["beans", "bread"],
                    "scrambled eggs": ["eggs", "butter", "milk"],
                    "soup": ["tin of soup"],
                    "pasta": ["pasta", "cheese"]}
books["maintenance"] = {"stuck": ["oil"],
                        "loose": ["gaffer tape"]}

print(books["recipes"]["soup"])
print(books["recipes"]["scrambled eggs"])

print(books["maintenance"]["loose"])

for key in books.keys():
    print(key)

books.close()
