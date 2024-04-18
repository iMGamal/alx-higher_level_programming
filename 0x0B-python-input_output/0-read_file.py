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
    with open('""', 'r', encoding="utf-8") as f:
        data = f.readlines()
        print(data)
