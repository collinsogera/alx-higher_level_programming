#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    rem = number % 10
else:
    tmp = number * -1
    rem = (tmp % 10) * -1

if rem > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, rem))
elif rem == 0:
    print("Last digit of {} is {} and is 0".format(number, rem))
else:
    print("Last digit of {} is {} and is".format(number, rem), end=' ')
    print("less than 6 and not 0")
