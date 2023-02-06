#!/usr/bin/python3
"""Int rebel module"""


class MyInt(Int):
    """Int class"""
    def __eq__(self, other):
        """Overrides and inverts == operator"""
        return int(self) != int(other)

    def __ne__(self, other):
        """Overrides and inverts != operator"""
        return int(self) == int (other)
