#!/usr/bin/python3
def remove_char_at(str, n):
    for n in str:
        if n >= 0:
            copystr = str[:n] + str[n + 1]
            return copystr
        else:
            return str
