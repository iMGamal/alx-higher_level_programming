#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
<<<<<<< HEAD
n = str(number)
if n != NULL:
    if n[0] == '-' and int(n[-1]) != 0:
        print(f"Last digit of {number} is -{n[-1]} and is less than 6 and not 0")
    elif n[0] != '-' and int(n[-1]) > 5:
        print(f"Last digit of {number} is {n[-1]} and is greater than 5")
    elif n[0] != '-' and int(n[-1]) < 6 and int(n[-1]) != 0:
        print(f"Last digit of {number} is {n[-1]} and is less than 6 and not 0")
    elif int(n[-1]) == 0:
        print(f"Last digit of {number} is {n[-1]} and is 0")
=======
n = abs(number) % 10

if number < 0:
    n = -n

if n > 5:
    print(f"Last digit of {number} is {n} and is greater than 5")
elif n < 6 and n != 0:
    print(f"Last digit of {number} is {n} and is less than 6 and not 0")
else:
    print(f"Last digit of {number} is {n} and is 0")
>>>>>>> 45b39aba433954ac6c029c13fab51eb17277776b
