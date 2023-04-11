#!/usr/bin/python3
"""An instance of a class of an inherited class"""


def is_kind_of_class(obj, a_class):
    """
    Return:
        True: if obj and class same instance
        False: if obj and class is not same instance
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
