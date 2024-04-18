#!/usr/bin/python3

"""defining write_file function."""


def write_file(filename="", text=""):
    """
    writes filename with utf-8 encoding.

    Return:
    - int: the number of characters written.
    """
    with open(filename, 'w', encoding="utf-8") as f:
    print(f.write(text), end="")
