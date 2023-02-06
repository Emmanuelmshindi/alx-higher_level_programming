#!/usr/bin/python3
"""Object instance module"""


def is_same_class(obj, a_class):
    """Is same class
    Returns:True if object is exactly an instance of the class.
    Otherwise-false"""
    return type(obj) == a_class
