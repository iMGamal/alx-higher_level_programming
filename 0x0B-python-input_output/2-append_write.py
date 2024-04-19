#!/usr/bin/python3

"""
defining function that appends to files.
"""


def append_write(filename="", text=""):
    """
    Args:
        filename (str): the string of text to beappended
        text (str): the string to be appended
    Return:
        characters (int): the numbers of characters added
    """
    with open(filename, "a", encoding="utf-8") as f:
        return (f.append(text))
