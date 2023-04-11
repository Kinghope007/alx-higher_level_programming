#!/usr/bin/python3
""" An empty class """


class BaseGeometry():
    """ This is empty class """
    pass

    def area(self):
        """method not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate a value as an integer """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value < 1:
            raise ValueError("{} must be greater than 0".format(name))
