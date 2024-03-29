#!/usr/bin/python3
""" A module that defines a square """
class Square:
    """ A class that represents a square """
    def __init__(self, size=0):
        """Initializing this square Class
        Args:
            size: represents the size of square defined
        Raise:
            TypeError: if size is not integer
            ValueError: if size is less than zero
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    def area(self):
        """
        Calculate area of the square
        Returns: the square of the size
        """
        return (self.__size ** 2)
