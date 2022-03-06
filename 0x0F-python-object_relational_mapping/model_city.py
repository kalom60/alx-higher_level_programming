#!/usr/bin/python3

"""
    a python file that contains the class definition
    of a City and an instance Base = declarative_base()
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String

Base = declarative_base()


class City(Base):
    """
        City class inherits the Base class

        Attributes:
            id (int)
            name (string)
            state_id (int)
    """

    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
