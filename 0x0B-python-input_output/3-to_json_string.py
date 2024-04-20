#!/usr/bin/python3
import json
"""
defining a json string.
"""


def to_json_string(my_obj):
    """
    Args:
        my_obj (str): a string to be converted to json style.
    Return:
        json represntation of an object (string).
        """
   return (json.dumps(my_obj))
