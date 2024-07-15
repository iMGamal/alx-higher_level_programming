#!/usr/bin/python3
"""
Module to disassemble python code.
"""
from dis import disassemble

def magic_calculation(a, b):
    return 98 + a ** b

disassemble(magic_calculation.__code__)
