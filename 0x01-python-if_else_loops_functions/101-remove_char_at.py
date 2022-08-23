#!/usr/bin/python3
def remove_char_at(str, n):
    a = ""
    b = 0
    new = len(str)
    if n < 0 or new < n:
        return str
    else:
        while new > b:
            if n == b:
                b += 1
                continue
            a += str[b]
            b += 1
        return b
