#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    last_number = ((number * -1) % 10) * -1
else:
    last_number = number % 10
if last_number > 5:
    out = "Last digit of {:d} is {:d} and is greater than 5"
elif last_number == 0:
    out = "Last digit of {:d} is {:d} and is 0"
else:
    out = "Last digit of {:d} is {:d} and is less than 6 and not 0"
print(out.format(number, last_number))
