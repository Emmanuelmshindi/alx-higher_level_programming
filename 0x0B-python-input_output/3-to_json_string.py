#!/usr/bin/python3
"""Module containing the function to_json_string."""
import json


def to_json_string(my_obj):
    """Returns JSON representation of an obj(string)

    Args:
        my_obj: the string

    Returns:
        str: string's JSON format
    """
    # print("type json.dumps(my_obj)--> {}".format(type(json.dumps(my_obj))))
    # print("type my_obj--> {}".format(type(my_obj)))

    # serializing json
    return json.dumps(my_obj)
