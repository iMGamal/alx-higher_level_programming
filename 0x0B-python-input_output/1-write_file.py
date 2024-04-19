#!/usr/bin/python3

"""
Defining a writing function.
"""


def write_file(filename="", text=""):
    """
    sfhjkkkkl
    """
    with open(filename, encoding="utf-8") as f:
        print(f.write(text))

