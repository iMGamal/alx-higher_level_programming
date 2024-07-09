#!/usr/bin/python3
"""
Module name : json
"""
import json


def to_json_string(my_obj):
    """
        Returns the JSON reprenstation of a string object.
    """
   return json.dumps(my_obj)
