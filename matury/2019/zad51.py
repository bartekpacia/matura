from zad5boiler import *

counter = 0

first_day = 0
last_day = 0
prev_temp = 0

for d in data:
  if d.temp >= 20 and d.rain <= 5:
    counter += 1

  if d.temp > prev_temp:
    first_day = d.day
  else:
    last_day = d.day

  prev_temp = d.temp


print(counter)
print(first_day, last_day)