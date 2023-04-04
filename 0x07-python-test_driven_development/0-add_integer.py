#!/usr/bin/python3
"""A modeule that that supplies the fucntion add_integer(a, b=89)"""
def add_integer(a, b=89):
    """ adds up two integer or floats
    Args:
        a: first argument
        b: second argument
    Raises:
        TypeError: either of arguments are not integer or float
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return (a + b)
