from enemy import Enemy, Troll, Vampire, VampireKing

ugly_troll = Troll("Pug")
print("Ugly troll - {}".format(ugly_troll))

another_troll = Troll("Ug")
print("Another troll - {}".format(another_troll))

brother = Troll("Urg")
print(brother)

ugly_troll.grunt()
another_troll.grunt()
brother.grunt()

awaken_vampire = Vampire("Sleepy")
print(awaken_vampire)
awaken_vampire.take_damage(10)
print(awaken_vampire)
awaken_vampire.take_damage(5)
print(awaken_vampire)
ugly_troll.take_damage(25)
print(ugly_troll)

vlad = VampireKing("Vlad The King")

while vlad._alive:
    vlad.take_damage(20)
    # print(awaken_vampire)
