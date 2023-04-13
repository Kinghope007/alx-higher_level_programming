#!/usr/bin/python3
"""
THis module defines a class student
"""


class Student:
    """
    represent a students information
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialiazes a new student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Gets a dictionary representation of the student
        """
        return self.__dict__
