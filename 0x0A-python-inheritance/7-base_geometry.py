#!/usr/bin/python3
"""BaseGeomerty class module"""


class BaseGeometry():
    """BaseGeometry class"""
    def area(self):
        """Raises an exception"""
        raise exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
