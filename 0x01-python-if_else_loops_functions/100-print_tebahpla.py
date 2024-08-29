#!/usr/bin/python3
for letter in reversed(range(97, 123)):
    if letter % 2 != 0:
        letter = chr(letter).upper()
    else:
        letter = chr(letter)
    print("{:s}".format(letter), end="")
