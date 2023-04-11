#!/usr/bin/python3
""" a class MyList that inherit list"""


class MyList(list):
    """A class that inherit from list"""
    def print_sorted(self):
        """ print sorted integer """
        print(sorted(self))
