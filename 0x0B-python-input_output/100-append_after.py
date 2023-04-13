#!/usr/bin/python3
"""
This module defines a text file insertion function
"""


def append_after(filename="", searching_string="", new_string=""):
    """
    Insert text after each line containing a given string
    """
    text = ""
    with open(filename) as _file:
        for line in _file:
            text += line
            if searching_string in line:
                text += new_string
    with open(filename, "w") as r:
        return r.write(text)
