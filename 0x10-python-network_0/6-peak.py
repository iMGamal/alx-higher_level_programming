#!/usr/bin/python3
"""Find peak element in an unsorted list."""


def find_peak(list_of_integers):
    """Find peak element in an unsorted list."""
    low = 0
    high = len(list_of_integers) - 1
    while low < high:
        mid = (low + high) // 2
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            low = mid + 1
        else:
            high = mid
    return list_of_integers[low]
