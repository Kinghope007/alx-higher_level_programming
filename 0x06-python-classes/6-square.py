#!/usr/bin/python3
""" A square module """
class Square:
    """ Define a class square """
    def __init__(self, size=0, position=(0, 0)):
        """ Create a square
        Args:
            size: length of a side of a square
            position: where the square is coordinates
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """ The property of size as the length of a side of square
        Raise:
            TypeError: if size != int
            ValueError: if size < 0
        return size
        """
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        """property of the coordinates of the square
        Raise:
                TypeError: if value != a tuple of integer < 0
        """

    @position.setter
    def position(self, value):
        """ property of the coordinates of this square
        Raise:
            TypeError: must be a tuple of 2 positive integers
        """
        if not isinstance(value, tuple):
            raise TypeError('position must be a tuple of 2 positive integers')
        if len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if len([i for i in value if isinstance(i, int) and i >= 0]) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """ Get the area of a square
        Return: the size of a squate
        """
        return (self.__size * self.__size)

    def my_print(self):
        """Print the square with the # character."""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
