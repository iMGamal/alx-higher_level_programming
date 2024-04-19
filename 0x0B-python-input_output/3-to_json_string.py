#!/usr/bin/python3

"""
defining a json string.
"""


def to_json_string(my_obj):
    """
    Args:
        my_obj (str): a string to be converted to json style.
    Return:
        json (str): JSON represntation of a strong.
    """
    with open(my_obj, "w", encoding="utf-8") as f:
        f = '{{"my_obj": "{}"}}'.format(my_obj)
        return (f.write())
