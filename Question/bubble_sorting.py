import random
import time


def bubble_sort(lst):
    # Check the Length of the given array
    len_arr = len(lst)

    copies = 0
    comparisons = 0
    # Start to sorting the Array.
    for i in range(len_arr - 1):
        for j in range(len_arr - 1 - i):

            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                copies += 2

    # Returning the Array
    return lst


def user_prompt():
    arr_elem = int(input('\x1b[6;30;42m' + 'Number of Elements in the Array:' + '\x1b[0m' + ' '))
    return [int(input(f"Enter Elem {ArrNum}: ")) for ArrNum in range(arr_elem)]


if __name__ == '__main__':
    try:
        the_arr = user_prompt()
        sorted_arr = bubble_sort(the_arr)
        print('\33[32m' + '\n\nAnd Here is the Sorted Array: ' + '\033[0m')
        print(f'\t--> \33[34m{sorted_arr}\033[0m')
    except:
        print('\033[91m' + "Error!!!, Hmm Something Went Wrong!!!" + '\033[0m')
