#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
stampa = ("Last digit of" + " " + str(number) + " " + "is" + " ")
if number > 0:
    while number % 10 > 5:
        print(stampa + str(number % 10) + " " + "and is greater than 5")
        break
    while number % 10 == 0:
        print(stampa + str(number % 10) + " " + "and is 0")
        break
    while number % 10 < 6 and number % 10 != 0:
        print(stampa + str(number % 10) + " " + "and is less than 6 and not 0")
        break
elif number < 0:
    while number % -10 < 6 and number % 10 != 0:
        print(stampa + str(number % -10) + " " + "and is less than 6 and not 0")
        break
