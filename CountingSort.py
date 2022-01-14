
from random import randint
from math import inf

def CountSort(Arr):
    arrLen = len(Arr)
    arrMax = max(Arr)
    arrMin = min(Arr)

    if Arr == []:
        return []

    CountLen = arrMax + 1 - arrMin
    Count = [0] * CountLen

    for Val in Arr: Count[Val - arrMin] += 1
    for i in range(1, CountLen): Count[i] = Count[i] + Count[i-1]

    SortedArr = [0] * arrLen

    for i in reversed(range(0, arrLen)):
        SortedArr[Count[Arr[i]-arrMin]-1] = Arr[i]
        Count[arr[i]-arrMin] -= 1
    
    return SortedArr



def counting_sort(arr, n, k, key=lambda x: x):
    counting_arr = [[] for i in range(k+1)] # O(k)
    sorted_arr = [] # O(1)
    for i in arr: # O(n)
        counting_arr[key(i)].append(i) # O(1) => stable sort
    for c in counting_arr: # O(k)
        sorted_arr.extend(c) # O(len(c))
    return sorted_arr

if __name__ == '__main__':
    # UserArr = [4, 2, 2, 8, 3, 3, 12]
    # AnsArr = CountSort(UserArr)
    # print(AnsArr)
    n = 10
    k = 100
    arr = [randint(0, k) for i in range(n)]
    print(arr)
    sorted_arr = CountSort(arr)
    print("arr: {}".format(arr))
    print("sorted_arr: {}".format(sorted_arr))
    