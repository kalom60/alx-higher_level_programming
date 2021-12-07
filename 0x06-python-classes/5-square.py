#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """Represents a square

    Attributes:
        __size (int): size of a side of the square.
    """

    def __init__(self, size=0):
        """initializes the square

        Args:
            size (int): size of a side of the square

        Returns:
            None
        """

        if isinstance(size, int) and size >= 0:
            self.__size = size
        elif not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    @property
    def size(self):
        """getter of __size

        Returns:
            The size of the square
        """

        return self.__size

    @size.setter
    def size(self, value):
        """setter of __size

        Args:
            value (int): size of a side of the square

        Returns:
            None
        """

        if isinstance(value, int) and value >= 0:
            self.__size = value
        elif not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """calculates the square's area

        Returns:
            The area of the square
        """

        return self.__size ** 2

    def my_print(self):
        """prints the square

        Returns:
            None
        """

        if not self.__size:
            print()
        else:
            for x in range(self.__size):
                for y in range(self.__size):
                    print("#", end='')
                print()
