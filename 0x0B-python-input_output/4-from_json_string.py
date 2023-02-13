#!/usr/bin/python3
"""Module containing the function from_json_string"""
import json


def from_json_string(my_str):
    """ returns an object (Python data structure) represented by a JSON string.

    Args:
        my_str: JSON string

    Returns:
        Object(python data structure)
    """
    # print("type json.loads(my_str)--> {}".format(type(json.loads(my_str))))
    # print("type my_str--> {}".format(type(my_str)))
    return json.loads(my_str)
