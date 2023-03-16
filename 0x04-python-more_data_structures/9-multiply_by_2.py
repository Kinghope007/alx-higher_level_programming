#!/usr/bin/python3
def multiple_by_2(a_dictionary):
    new = list(a_dictionary.key())

    for i in new:
        new[i] *= 2
    return (new)
