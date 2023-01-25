#!/usr/bin/python3
""" creates class Square """


class Square:
    """
    Class that defines proprties of square
    Attributes:
        size: size of a square (1 side).
    """
    def __init__(self, size=0):
        """Creates new instances of square.
        Args:
            size: size of the square (1 side).
        """
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ Calculates the area of the square

            Returns the current square area 
        """
        return self.__size ** 2
