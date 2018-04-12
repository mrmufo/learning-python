from player import Player

woj = Player("Woj")

print(woj.name)
print(woj.lives)
woj.lives -= 1
print(woj)

woj.lives -= 1
print(woj)

woj.lives -= 1
print(woj)
woj.lives -= 1
print(woj)

woj.level += 1
print(woj)
woj.level += 1
print(woj)
woj.level -= 2
print(woj)
woj.level -= 1
print(woj)