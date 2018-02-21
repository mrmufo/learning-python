# Create a program that allows a user to choose one of
# up to 9 time zones from a menu. You can choose any
# zones you want from the all_timezones list.
#
# The program will then display the time in that timezone, as
# well as local time and UTC time.
#
# Entering 0 as the choice will quit the program.
#
# Display the dates and times in a format suitable for the
# user of your program to understand, and include the
# timezone name when displaying the chosen time.

import datetime
import pytz

menu = {1: "Andorra",
        2: "Burundi",
        3: "Belarus",
        4: "Iran",
        5: "St Kitts & Nevis",
        6: "Maldives",
        7: "Poland",
        8: "Palau",
        9: "Great Britain"}

menu_tz = {1: "Europe/Andorra",
           2: "Africa/Bujumbura",
           3: "Europe/Minsk",
           4: "Asia/Tehran",
           5: "America/St_Kitts",
           6: "Indian/Maldives",
           7: "Europe/Warsaw",
           8: "Pacific/Palau",
           9: "Europe/London"}

chosenCountry = 10

while True:
    for each in menu:
        print("{number}: {country}".format(number=each, country=menu.get(each)), end=', ')

    chosenCountry = int(input("\nChoose a number of the country to see its time: (0 to quit)\n"))
    if chosenCountry == 0:
        break

    if chosenCountry in menu.keys():
        cc_time = menu_tz.get(chosenCountry)
        local_time = pytz.utc.localize(datetime.datetime.now()).astimezone()
        utc_time = pytz.utc.localize(datetime.datetime.utcnow()).astimezone()
        countryTimeZone = pytz.timezone(cc_time)
        countryTime = local_time.astimezone(countryTimeZone)

        print("=" * 100)
        print("Your local time:\t{lt}, time zone {lttz} \nUTC time:\t\t\t{utc}, time zone {utctz}\n"
              "Time in {country}:\t\t{ct}, time zone {ctz}"
              .format(lt=local_time, lttz=local_time.tzinfo, utc=utc_time, utctz=utc_time.tzinfo,
                      country=menu.get(chosenCountry), ct=countryTime, ctz=countryTime.tzinfo))
        print("=" * 100)
    else:
        print("Wrong input, try again")
