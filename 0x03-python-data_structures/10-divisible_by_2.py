#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    _div = []

    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            _div.append(True)
        else:
            _div.append(False)
    return _div
