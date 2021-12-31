#!/usr/bin/python3
"""Define a square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent the square"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new square object

        Args:
            size (int): The size of the new square
            x    (int): x coordinate of the new square
            y    (int): y coordinate of the new square
            id   (int): id of the new square
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get the size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the square"""
        self.width = value
        self.height = value

    def __str__(self):
        """Return the print() and str() representation of a Square."""
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x,
                                                 self.y,
                                                 self.width)
