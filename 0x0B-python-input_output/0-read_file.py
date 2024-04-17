#!/usr/bin/python3
"""You are not allowed to import any modules."""


def read_file(filename=""):
"""Prototype for a function that reads files."""
    with open('""', 'r', encoding="utf-8") as f:
        data = f.readlines()
        print(data)
