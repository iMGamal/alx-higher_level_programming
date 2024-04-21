#!/usr/bin/python3
"""Module provides functions for dealing with JSON data"""
import json


def to_json_string(my_obj):
    """Returns the JSON reprenstation of a string object."""
   return json.dumps(my_obj)
