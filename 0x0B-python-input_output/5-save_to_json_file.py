#!/usr/bin/python3
"""Module containing the function save_to_json_file"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file

    Args:
        my_obj: JSON object
        filename: file to write into

    Returns:
        type: JSON representation.
    """

    # print("type of json_object --> {}".format(type(json_object)))
    # print("type of my_obj --> {}".format(type(my_obj)))
    # print("type file name --> {}".format(type(filename)))
    # writing to file
    with open(filename, 'a', encoding="utf-8") as f:
        #serializing json
        json object =  json.dumps(my_obj)
        # or json.dump(my_obj, f)
        f.write(json_object)
        f.close()
