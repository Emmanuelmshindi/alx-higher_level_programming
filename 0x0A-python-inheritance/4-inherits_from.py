#!/usr/bin/python3
"""Module containing inherits from method"""


def inherits_from(obj, a_class):
    """Returns:
    True if object is an instance of a class that inherited from
    the specified class. Otherwise false."""
    return isinstance(obj, a_class) and type(obj) != a_class
