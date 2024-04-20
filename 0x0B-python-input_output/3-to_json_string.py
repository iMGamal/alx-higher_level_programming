#!/usr/bin/python3
import json
"""
defining to_json_string function.
"""


def to_json_string(my_obj):
    """
    serializing an object to json formatted string.
    """
   return (json.dumps(my_obj))
