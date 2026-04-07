#!/usr/bin/python3
"""
Square module
"""


class Square:
    """
    Square class
    """

    def __init__(self, size=0):
        """
        Initialize square
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieve size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set size with validation
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Returns the current square area
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square with the # character
        """
        if self.__size == 0:
            print("")
            return

        for i in range(self.__size):
            print("#" * self.__size)
