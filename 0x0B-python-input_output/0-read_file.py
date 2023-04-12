#!/usr/bin/python3
""" THis module definesa text reading module function"""


def read_file(filename=""):
    """prints content of a file """
    with open(filename, encoding="utf-8") as _file:
        print(_file.read(), end="")
