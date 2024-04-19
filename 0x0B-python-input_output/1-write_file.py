#!/usr/bin/python3
"""
Defining a writing function.
"""


def write_file(filename="", text=""):
    """Function that writes a string with utf-8 encoding.
    Args:
        filename (str): the file passed to function.
        text (str): the new string to be written.
    Return:
        The number of characters written.
    """
    with open(filename, encoding="utf-8") as f:
        print(f.write(text) + end="")
