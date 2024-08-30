#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv

operators = ['+', '-', '*', '/']
if __name__ == "__main__":
    if (len(argv) - 1) != 3:
        print("Usage: ./100-my_calaculator.py <a> <operator> <b>\n1")
    elif (len(argv) - 1) == 3 and argv[2] not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
    elif (len(argv) - 1) == 3 and argv[2] in operators:
        print(str(argv[1]) + " " + str(argv[2]) + " = " + "{:s}".format(str(argv[3]))
