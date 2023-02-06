#!/usr/bin/python3
"""Rectangle class module"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Square(Rectangle):
    """Square class"""
    def __init__(self, size):
        """Initialize square method"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Method that returns area of a square"""
        return "self.__size ** 2
