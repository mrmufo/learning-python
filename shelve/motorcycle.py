import shelve

with shelve.open("bike") as bike:
    # bike["make"] = "Honda"
    # bike["model"] = "CB 500"
    # bike["colour"] = "red"
    # bike["engine_size"] = 500

    # del bike['engin_size']

    for key in bike:
        print(key)

    print('=' * 40)

    print(bike["engine_size"])
    # print(bike["engin_size"])
    print(bike["colour"])
