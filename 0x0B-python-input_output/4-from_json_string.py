#!/usr/bin/python3
"""This module defnies a JSOn re[presentation to object function"""
import json

def from_json_string(my_str):
    """
    Returns the pytohn object representation of a JSON structure
    """
    return json.loads(my_str)
