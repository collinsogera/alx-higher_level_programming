#!/usr/bin/python3
def roman_to_int(roman_string):
    number = 0
    if roman_string is None or isinstance(roman_string, str) is False:
        return 0
    for i in range(len(roman_string)):
        if roman_string[i] == "M":
            number += 10000

