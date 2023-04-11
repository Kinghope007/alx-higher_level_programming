#!/usr/bin/python3
"""A rectangle class inherorting from BAseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class to defnies rectangle using BaseGeometry"""

    def __init__(self, width, height):
        """Instantiation"""
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
