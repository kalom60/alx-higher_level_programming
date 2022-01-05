#!/usr/bin/python3
"""Define a base model class"""
import json
import csv
import turtle


class Base:
    """Represent the base model

    Represents the "base" for all other classes in the project

    Attributes:
        __nb_objects (int): The number of instantiated Bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base

        Args:
            id (int): The id of the new base
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON serialization of a list of dicts

        Args:
            list_dictionaries (list): A list of dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON serialization of a list of objects to a file

        Args:
            list_objs (list): A list of inherited Base instances
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            if list_objs is None:
                f.write(str([]))
            else:
                list_dicts = [i.to_dictionary() for i in list_objs]
                f.write(str(Base.to_json_string(list_dicts)))

    @staticmethod
    def from_json_string(json_string):
        """Return the deserialization of a JSON string

        Args:
            json_string (str): A JSON str representation of a list of dicts

        Returns:
            If json_string is None or empty - an empty list
            else - the Python list represented by json_string
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return a class instantied from a dictionary of attributes

        Args:
            **dictionary (dict): Key/value pairs of attributes to initialize
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """Return a list of classes instantiated from a file of JSON strings

        Reads from '<cls.__name__>.json'

        Returns:
            If the file does not exist - an empty list
            else - a list of instantiated classes
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as f:
                list_dicts = Base.from_json_string(f.read())
                return [cls.create(**dicts) for dicts in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write the CSV serialization of a list of objects to a file

        Args:
            list_objs (list): A list of inherited Base instances
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as f:
            if list_objs is None or list_objs == []:
                f.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fields = ["id", "width", "height", "x", "y"]
                else:
                    fields = ["id", "size", "x", "y"]
                to_write = csv.DictWriter(f, fieldnames=fields)
                for obj in list_objs:
                    to_write.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of classes instantiated from a CSV file

        Reads from '<cls.__name__>.csv'

        Returns:
            If the file does not exist - an empty list
            else - a list of instantiated classes
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as f:
                if cls.__name__ == "Rectangle":
                    fields = ["id", "width", "height", "x", "y"]
                else:
                    fields = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(f, fieldnames=fields)
                list_dicts = [
                    dict([k, int(v)] for k, v in dicts.items()) for dicts in list_dicts
                ]
                return [cls.create(**dicts) for dicts in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Opens a window and draws all the Rectangles and Squares

        Args:
            list_rectangles (list): list values of a rectangle
            list_squares    (list): list values of a square
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#2e2e2e")
        turt.pensize(4)

        turt.color("#6879a4")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b93030")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
