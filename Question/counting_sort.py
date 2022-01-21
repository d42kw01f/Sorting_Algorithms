def counting_sort(arr, n):
    auxi_arr = [0] * n

    for val in arr:
        num_less_elem = 0
        for elem in arr:
            if elem < val:
                num_less_elem += 1
        auxi_arr[num_less_elem] = val

    return auxi_arr


def unique_values(g):
    s = set()
    for x in g:
        if x in s:
            return False
        s.add(x)
    return True


def user_prompt():
    arr_elem = int(input('\x1b[6;30;42m' + 'Number of Elements in the Array:' + '\x1b[0m' + ' '))
    return [int(input(f"Enter Elem {ArrNum}: ")) for ArrNum in range(arr_elem)]


if __name__ == '__main__':
    try:
        the_arr = user_prompt()
        len_arr = len(the_arr)
        if not unique_values(the_arr):
            print('\33[5m\n\tOnly distinct integers are allowed\33[6m')
            exit()
        sorted_arr = counting_sort(the_arr, len_arr)
        print('\33[32m' + '\n\nAnd Here is the Sorted Array: ' + '\033[0m')
        print(f'\t--> \33[34m{sorted_arr}\033[0m')
    except:
        print('\033[91m' + "Error!!!, Hmm Something Went Wrong!!!" + '\033[0m')
