#!/usr/bin/python3

""" This script contains the class definition of a State and an instance
    Base=Declarative base()
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
        State class inherits base class
        Attributes:
            id (int)
            name (str)
    """

    __tablename__ = 'states'

    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
