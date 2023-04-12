#!/usr/bin/python3
"""THis module defines a JSON file-writing function"""
import json


def save_to_json_file(my_obj, filename):
    """
    writes an object to a text file using JSON format
    """
    with open(filename, "w") as _file:
        return json.dump(my_obj, _file)
