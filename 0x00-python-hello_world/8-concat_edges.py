#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
         language that combines remarkable power with very clear syntax"
str = str.split()[5][0:7] + str.join('\n') + str.split()[5][7:] + str.join(' ') + str.split()[6] + str.join(' ') + str.split()[12] + str.join(' ') + str.split()[0]
print(str)