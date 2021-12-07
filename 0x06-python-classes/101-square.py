#!/usr/bin/python3
"""Define a class Square"""


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
            position (tuple): positoin of the square

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

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """getter of __position

        Returns:
            The position of the square in 2D space
        """

        return self.__position

    @position.setter
    def position(self, value):
        """setter of __position

        Args:
            value (tuple): position of the square

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

        return (self.__size ** 2)

    def my_print(self):
        """prints the square

        Returns:
            None
        """

        if self.size == 0:
            print()
        else:
            for i in range(self.position[1]):
                print()
            for i in range(0, self.size):
                for k in range(self.position[0]):
                    print(" ", end='')
                for j in range(self.size):
                    print("#", end='')
                print()

    def __str__(self):
        """String representation of a Square instance

        Returns:
            Formatted string representing the square
        """

        rn = ""

        if self.size == 0:
            return rn

        for i in range(self.position[1]):
            rn += "\n"

        for i in range(0, self.size):
            for k in range(self.position[0]):
                rn += " "
            for j in range(self.size):
                rn += "#"
            if i is not (self.size - 1):
                rn += "\n"

        return rn
