#!/usr/bin/python3
"""Check if object isstance of class"""


def is_same_class(obj, a_class):
    """Returns:
        True: if object and class are same instance
        False: if object and class are not same instance
    """
    return (type(obj) == a_class)
