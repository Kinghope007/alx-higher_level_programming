#!/usr/bin/python3
"""defines a rectangle subclass square. """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square"""

    def __init__(self, size):
        """Instantiation"""
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
