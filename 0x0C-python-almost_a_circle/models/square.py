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

    def update(self, *args, **kwargs):
        """Update the square

        Args:
            *args (ints): new attribute values
                - 1st argument should be the id attribute
                - 2nd argument should be the size attribute
                - 3rd argument should be the x attribute
                - 4th argument should be the y attribute
            **kwargs(dict): New key-value pairs of attributes
        """
        if args and len(args) != 0:
            num = 0
            for arg in args:
                if num == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif num == 1:
                    self.size = arg
                elif num == 2:
                    self.x = arg
                elif num == 3:
                    self.y = arg
                num += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Return the dictionary representation of the Square"""
        return {
                    "id": self.id,
                    "size": self.width,
                    "x": self.x,
                    "y": self.y
                }
