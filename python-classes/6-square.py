#!/usr/bin/python3
"""
Square module
"""


class Square:
    """
    Square class
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize square
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        Retrieve position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set position with validation
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Returns the current square area
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square with the # character and position
        """
        if self.__size == 0:
            print("")
            return

        # Yuxarıdan buraxılan boşluqlar (Y koordinatı)
        if self.__position[1] > 0:
            for _ in range(self.__position[1]):
                print("")

        # Kvadratın sətirləri
        for _ in range(self.__size):
            # Soldan buraxılan boşluqlar (X koordinatı)
            print(" " * self.__position[0] + "#" * self.__size)
