#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

a = 10
b = 5

if __name__ == "__main__":
    result0 = add(a, b)
    print(str(a) + " + " + str(b) + " = " + "{:s}".format(str(result0)))
    result1 = sub(a, b)
    print(str(a) + " - " + str(b) + " = " + "{:s}".format(str(result1)))
    result2 = mul(a, b)
    print(str(a) + " * " + str(b) + " = " + "{:s}".format(str(result2)))
    result3 = div(a, b)
    print(str(a) + " / " + str(b) + " = " + "{:s}".format(str(result3)))
