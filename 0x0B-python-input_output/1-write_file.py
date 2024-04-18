#!/usr/bin/python3
"""Defining write_file function."""


def write_file(filename="", text=""):
    """Writes filename with utf-8 encoding.
    Return:
    - int: the number of characters written.
    """
    with open(filename, 'w', encoding="utf-8") as f:
    print(f.write(text), end="")
