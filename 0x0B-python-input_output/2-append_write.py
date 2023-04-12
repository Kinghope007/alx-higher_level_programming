#!/usr/bin/python3
""" This file defines a file appending function"""


def append_write(filename="", text=""):
    """
    Appends a string to yht end og a UTF* text file
    """
    with open(filename, "a", encoding="utf-8") as _file:
        return _file.write(text)
