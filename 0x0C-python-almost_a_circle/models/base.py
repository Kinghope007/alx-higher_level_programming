#!/usr/bin/python3
"""
THis module contain a class to serve as base for other classes
"""


import csv
import json
import os


class Base:
    """
    Represents base of all classes created
    """
    _nb_objects = 0

    def __init__(self, id=None):
        """
        Initilaiing id
        """
        if id is not None:
            self.id = id
        else:
            Base._nb_objects += 1
            self.id = Base._nb_objects
