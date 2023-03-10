#!/usr/bin/python3

def multiple_returns(setence):
    str_len = len(sentence)

    if len(sentence) == 0:
        first_char = None
    else:
        first_char = sentence[0]
    _tuple = (len(sentence), first_char)
    return _tuple
