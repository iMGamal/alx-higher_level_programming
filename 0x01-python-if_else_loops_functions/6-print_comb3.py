#!/usr/bin/python3
i = 0
while i < 10:
    j = 0
    while j < 10:
        if i == 0 and i != j:
            print("{}".format(str(i)) + "{}".format(str(j)), end=", ")
        if i > 0 and i <= 7 and i < j:
            print("{}".format(str(i)) + "{}".format(str(j)), end=", ")
        elif i == 8 and i < j:
            print("{}".format(str(i)) + "{}".format(str(j)), end="\n")
        j += 1
    i += 1
