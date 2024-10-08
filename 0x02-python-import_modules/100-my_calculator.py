#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv

operators = ['+', '-', '*', '/']
if __name__ == "__main__":
    if (len(argv) - 1) != 3:
        print("./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif (len(argv) - 1) == 3 and argv[2] not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    elif (len(argv) - 1) == 3 and argv[2] in operators:
        if argv[2] == '+':
            result = add(int(argv[1]), int(argv[3]))
            x = argv[1]
            y = argv[2]
            z = argv[3]
            print(str(x) + " " + str(y) + " " + str(z) + " = " + str(result))
        elif argv[2] == '-':
            result = sub(int(argv[1]), int(argv[3]))
            x = argv[1]
            y = argv[2]
            z = argv[3]
            print(str(x) + " " + str(y) + " " + str(z) + " = " + str(result))
        elif argv[2] == '*':
            result = mul(int(argv[1]), int(argv[3]))
            x = argv[1]
            y = argv[2]
            z = argv[3]
            print(str(x) + " " + str(y) + " " + str(z) + " = " + str(result))
        elif argv[2] == '/':
            result = div(int(argv[1]), int(argv[3]))
            x = argv[1]
            y = argv[2]
            z = argv[3]
            print(str(x) + " " + str(y) + " " + str(z) + " = " + str(result))
