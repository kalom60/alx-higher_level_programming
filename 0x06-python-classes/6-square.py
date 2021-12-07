#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """Represents a square

    Attributes:
        __size (int): size of a size of the square
        __position (tuple): position of the square in 2D space
    """

    def __init__(self, size=0, position=(0, 0)):
        """initializes the square

        Args:
            size (int): size of a side of the square
            position (tuple): positoin of the square in 2D space

        Returns:
            None
        """

        self.size = size
        self.position = position

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

    @property
    def position(self):
        """getter of __position

        Returns:
            The position of the square
        """

        return self.__position

    @position.setter
    def position(self, value):
        """setter of __position

        Args:
            value (int): position of a side of the square

        Returns:
            None
        """

        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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

        if self.size == 0:
            print()
        else:
            for x in range(self.position[1]):
                print()
            for x in range(0, self.size):
                for y in range(self.position[0]):
                    print(" ", end='')
                for z in range(self.size):
                    print("#", end='')
                print()
