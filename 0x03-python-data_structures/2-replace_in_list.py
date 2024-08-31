#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0 or idx not in my_list:
        return 0
    my_list[idx] = element
