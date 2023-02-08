#!/usr/bin/python3
"""Module containing the function append_write"""


def append_write(filename="", text=""):
    """Appends string at the end of a text file and returns
    the number of characters added.

    Args:
        filename (str, optional): name of the file. Defaults to "".
        text (str, optional): string of text to append. Defaults to "".

    Returns:
        Returns number of characters added.
    """
    with open(filename, 'w', encoding="utf-8") as f:
        """This method returns the number of characters appended to a file."""
        return f.write(text)
