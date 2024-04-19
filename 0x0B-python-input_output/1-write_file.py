#!/usr/bin/python3

"""
Defining a writing function.
"""


def write_file(filename="", text=""):
    """
    Args:
        filename (str): the text to be overwritten.
        text (str): the new text to be written.
    Return:
        characters (int): the number of characters printed.
    """
    with open(filename, encoding="utf-8") as f:
        f.write(text)
        return (len(text))
