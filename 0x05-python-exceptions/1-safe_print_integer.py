#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    total = 0
    for i in range(x):
        try:
            print(f"{my_list[i]}", end="")
            total += 1
        except IndexError:
            break
    print()
    return(total)

if __name__ == '__main__':
    value = 89
    has_been_print = safe_print_integer(value)
    if not has_been_print:
        print("{} is not an integer".format(value))

    value = -89
    has_been_print = safe_print_integer(value)
    if not has_been_print:
        print("{} is not an integer".format(value))

    value = "Holberton"
    has_been_print = safe_print_integer(value)
    if not has_been_print:
        print("{} is not an integer".format(value))
