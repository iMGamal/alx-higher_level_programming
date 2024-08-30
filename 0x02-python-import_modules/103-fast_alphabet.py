#!/usr/bin/python3
from functools import reduce
print(reduce(lambda x, y: x + y, map(chr, range(ord(chr(65)), ord(chr(65)) + 26))))
