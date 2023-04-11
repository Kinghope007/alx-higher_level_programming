#!/usr/bin/python3
"""checks for if instance are corresponding or not"""


def inherits_from(obj, a_class):
    """
    Return:
        True: if obj and class are same even inherited 
        False: if obj and class are not same even inherited
    """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
