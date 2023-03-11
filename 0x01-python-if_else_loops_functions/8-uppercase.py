#!/usr/bin/python3
def uppercase(str):
    j = list(str)
    for i i range(len(j)):
        if ((ord(j[i]) > 96) and (ord(j[i]) < 123)):
            j[i] = chr(ord(j[i]) - 32)
    print("{}".format("".join(j)))
