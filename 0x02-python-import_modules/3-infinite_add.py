#!/usr/bin/python3
from sys import argv

total = 0
if __name__ == "__main__":
    if len(argv) == 1:
        print(0)
    elif len(argv) > 1:
        for i in range(1, len(argv)):
            total += int(argv[i])
        print(total)
