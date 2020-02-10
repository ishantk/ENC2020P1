# import datetime
import datetime as dt

today = dt.datetime.today()
print(today)
print(type(today))

# today = str(dt.datetime.today())

tomorrow = dt.datetime(2020, 2, 11, 13, 10, 5)
print(tomorrow)

print(tomorrow-today)