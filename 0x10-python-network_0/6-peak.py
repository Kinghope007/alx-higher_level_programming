#!/usr/bin/python3
"""
Algorithms for list of intergers.
"""


def find_peak(list_of_intergers):
    if not list_of_intergers:
        return None
    if list_of_intergers:
        list_of_intergers.sort(reverse=True)
        return list_of_intergers[0]
