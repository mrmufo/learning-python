import pytz
import datetime
country = 'Europe/Moscow'

tz_to_display = pytz.timezone(country)
local_time = datetime.datetime.now(tz=tz_to_display)
print("The time in {country} is {time}".format(country=country, time=local_time))
print("UTC is {UTC}".format(datetime.datetime.utcnow()))
