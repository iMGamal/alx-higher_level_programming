#!/usr/bin/python3
# function that prints elements of a list
def safe_print_list(my_list=[], x=0):
    my_list=[n]
    while x >= n:
        try:
            print(my_list)
            break
        except: x = 0
        print("invalid")
