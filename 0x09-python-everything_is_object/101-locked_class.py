#!/usr/bin/python3
""" This defines a lock class """


class LockedClass:
    """
    onlu allow installation of the attribute called first_name
    """

    __slots__ = ["first_name"]
