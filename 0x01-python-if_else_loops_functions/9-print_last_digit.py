#!/usr/bin/python3
def print_last_number(number):
    if number >= 0:
        rem = number % 10
    else:
        tmp = number * -1
        rem = (tmp % 10) * -1
    print("{}".format(rem))
