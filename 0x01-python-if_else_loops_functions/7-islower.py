#!/usr/bin/python3
def islower(c):
    if c.islower() is True:
        return c
    elif c == "":
        raise TypeError("string can't be empty")
    else:
        pass
