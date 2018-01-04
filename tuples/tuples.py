# # t = ("a", "b", "C")
# # print(t)
# #
# # print("a", "b", "c")
# # print(("a", "b", "c"))
# #
# welcome = "Welcome to my Nightmare", "Alice Cooper", 1975
# bad = "Bad Company" "Bad Company", 1974
# budgie = "Nightflight", "Budgie", 1981
# imelda = "More Mayhem", "Imelda May", 2011, (1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz")
#
# # metallica = "Ride the Lightning", "Metallica", 1984
#
# # print(metallica)
# # print(metallica[0])
# # print(metallica[1])
# # print(metallica[2])
# # imelda = imelda[0], "Imelda May", imelda[2]
# # print(imelda)
# #
# # metallica2 = ["Ride the Lightning", "Metallica", 1984]
# # print(metallica2)
# # metallica2[0] = "Master of Puppets"
# # print(metallica2)
# #
# # metallica2.append("Rock")  # title, artist, year = imelda
# #
# # title, artist, year = metallica2
# # print(title)
# # print(artist)
# # print(year)
# print(imelda)
#
# title, artist, year, track1, track2, track3, track4 = imelda
# print(title)
# print(artist)
# print(year)
# print(track1)
# print(track2)
# print(track3)
# print(track4)

# Given the tuple below that represents the Imelda May album "More Mayhem", write
# code to print the album details, followed by a listing of all the tracks in the album.
#
# Indent the tracks by a single tab stop when printing them (remember that you can pass
# more than one item to the print function, separating them with a comma).

imelda = "More Mayhem", "Imelda May", 2011, (
    (1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz"))
track = imelda[3]
print(imelda[0], imelda[1], imelda[2], "\n    {0}\n    {1}\n    {2}\n    {3}"
      .format(track[0], track[1], track[2], track[3]))
# =======================================or
title, artist, year, tracks = imelda
print(title, artist, year)
for song in tracks:
    track, title = song
    print("\tTrack number: {} \tTitle: {}".format(track, title))

# =======================================or
imelda = "More Mayhem", "Imelda May", 2011, (
    [(1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz")])

imelda[3].append((5, "All For You"))

title, artist, year, tracks = imelda
tracks.append((6, "Eternity"))
print(title, artist, year)
for song in tracks:
    track, title = song
    print("\tTrack number: {} \tTitle: {}".format(track, title))