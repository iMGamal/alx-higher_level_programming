#!/usr/bin/python3
from sys import argv

if len(argv) == 1:
    print("0" + " arguments.")
elif len(argv) == 2:
    print("{:s}".format(str(len(argv) - 1)) + " argument:")
    for i in range(1, len(argv)):
        print(str(i) + ": " + "{:s}".format(argv[i]))
elif len(argv) > 2:
    print("{:s}".format(str(len(argv) - 1)) + " arguments:")
    for i in range(1, len(argv)):
        print(str(i) + ": " + "{:s}".format(argv[i]))
