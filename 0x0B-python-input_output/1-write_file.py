#!/usr/bin/python3
"""This module defines a file-writing function"""


def write_file(filename="", text=""):
    """write a string to a UTF8 file and print out thr number of char"""
    with open(filename, "w", encoding="utf-8") as _file:
        return _file.write(text)
