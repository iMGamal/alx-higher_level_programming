#!/usr/bin/python3
"""Find peak element in an unsorted list."""


def find_peak(list_of_integers):
    """Find peak element in an unsorted list."""
    peak = list_of_integers[0]
    for i in list_of_integers[1:]:
        if i > peak:
            peak = i
    return peak
