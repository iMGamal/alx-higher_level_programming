#!/usr/bin/python3
def print_list_integer(my_list=[]):
    output = ["{:d}".format(i) for i in my_list]
    print(*output, sep="\n")
