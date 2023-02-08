#!/usr/bin/python3
"""Module containing the function write_file"""


def write_file(filename="", text=""):
    """Writes to a file and returns number of chars

    Args:
        filename (str, optional):name for file to write to.Defaults to "".
        text (str, optional): string of text to write to fileDefaults to "".
   
   Returns:
        int: number of characters written to a file.
    """
    with open(filename, 'r', encoding="utf-8") as f:
        """This method returns the number of characters written to a file."""
        return f.write(text)
