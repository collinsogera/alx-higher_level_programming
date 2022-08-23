#!/usr/bin/python3
def uppercase(str):
    index = 0
    while index < len(str):
        if ord(str[index]) >= ord('a') and ord(str[index]) <= ord('z'):
            new = chr(ord(str[index]) - 32)
        else:
            new = str[index]
        print("{:s}".format(new), end="")
        index += 1
    print()
