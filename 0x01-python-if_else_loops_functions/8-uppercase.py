#!/usr/bin/python3
def uppercase(str):
    result = ""
    for i in str:
        if ord(i) in range(ord('a'), ord('z') + 1):
            arg = ord(i)
            result += chr(arg - 32)
        else:
            result += i
    print(result)
