#!/usr/bin/python3
"""This module defines a string to JSON funtion"""
import json


def to_json_string(my_obj):
    """
    Returns a JSON representation of a string object
    """
    return json.dumps(my_obj)
