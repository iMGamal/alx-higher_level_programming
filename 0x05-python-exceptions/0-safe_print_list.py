def safe_print_list(my_list=[], x=0)
    my_list=[n]
    while x >= n:
        try:
            print(n)
        except:
            x = 0
            print("invalid input")
            break
        return x
    print(safe_print_list(my_list[1,2,3,4], x=4))
