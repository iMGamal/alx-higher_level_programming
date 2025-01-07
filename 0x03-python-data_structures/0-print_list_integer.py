#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """Print the list content in separate lines."""
    for i in my_list:
        print("{}".format(i))


print_list_integer([1, 2, 3, 4, 5])
