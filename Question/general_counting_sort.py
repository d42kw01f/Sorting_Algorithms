from random import randint
from math import inf


def count_sort(lst):
    if not lst:
        return []
    arr_len = len(lst)
    arr_max = max(lst)
    arr_min = min(lst)

    count_len = arr_max + 1 - arr_min
    count = [0] * count_len

    for Val in lst:
        count[Val - arr_min] += 1
    for i in range(1, count_len):
        count[i] += count[i - 1]

    sorted_array = [None] * arr_len

    for i in reversed(range(0, arr_len)):
        sorted_array[count[lst[i] - arr_min] - 1] = lst[i]
        count[lst[i] - arr_min] -= 1

    return sorted_array


def user_prompt():
    arr_elem = int(input('\x1b[6;30;42m' + 'Number of Elements in the Array:' + '\x1b[0m' + ' '))
    return [int(input(f"Enter Elem {ArrNum}: ")) for ArrNum in range(arr_elem)]


if __name__ == '__main__':
    try:
        the_arr = user_prompt()
        sorted_arr = count_sort(the_arr)
        print('\33[32m' + '\n\nAnd Here is the Sorted Array: ' + '\033[0m')
        print(f'\t--> \33[34m{sorted_arr}\033[0m')
    except:
        print('\033[91m' + "Error!!!, Hmm Something Went Wrong!!!" + '\033[0m')
