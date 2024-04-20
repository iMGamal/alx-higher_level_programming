#!/usr/bin/python3

"""
defining to_json_string function.
"""
import json


def to_json_string(my_obj):
    """
    serializing an object to json formatted string.
    """
   return (json.dumps(my_obj))
