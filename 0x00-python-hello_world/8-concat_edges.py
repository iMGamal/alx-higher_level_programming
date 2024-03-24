#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
         language that combines remarkable power with very clear syntax"
str = str[39:54] + str.join(' ') + str[55:66] + str.join(' ') + str[115:119] + str.join(' ') + str[:6]
print(str)
