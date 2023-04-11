#!/usr/bin/python3
"""this defines a class MyInt that inherit from int """


class MyInt(int):
    """ Invert int operators == and != """

    def __eq__(self, value):
        """Override == operator with != behavior"""
        return self.real != value

    def __ne__(self, value):
        """Overrides != operator with == behavoir"""
        return self.real == value
