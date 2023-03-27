#!/usr/bin/python3
def safe_print_list_interger(my_list=[], x=0):
    read = 0
    for j in range(x):
        try:
            print("{:d}".format(my_list[j], end="")
            read += 1
         except (ValueError, TypeError):
                    continue
    print()
    return(read)
