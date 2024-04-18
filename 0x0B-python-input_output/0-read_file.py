#!/usr/bin/python3

"""
defining read_file function.
"""


def read_file(filename=""):
    """
    reads filename with utf-8 encoding.

    Returns:
    - str: the result of reading.
    """
    with open(filename, encoding="utf-8") as f:
        data = f.read() + end""
        print(data)
