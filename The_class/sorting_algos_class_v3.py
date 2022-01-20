import random
import time
import inspect


class SortingAlgo:
    __slots__ = ['Arr', 'arrLen', 'arrMax', 'arrMin', 'select_comp']

    def __init__(self, arr_lst):
        self.Arr = arr_lst
        self.arrLen = len(arr_lst)
        self.arrMax = max(arr_lst)
        self.arrMin = min(arr_lst)
        self.select_comp = 0

    # This function allows to measure each algorithm runtime
    @staticmethod
    def timed(f):
        def _timed(*args, **kwargs):
            start = time.time()
            v = f(*args, **kwargs)
            the_time = time.time() - start
            print("---" * 50)
            print(f"--> Running Time of {f.__name__} Algorithm is: {str(the_time)}")
            return v

        return _timed

    @timed
    def selection_sort(self):
        # Travelling through all the elements in the given array
        sorted_arr_select = self.Arr.copy()
        select_comp = 0
        for i in range(self.arrLen):
            # bellow codes will allow to find the minimum element in the array
            min_elm = i
            for j in range(i + 1, self.arrLen):
                # Following code allows find total number of comparisons, made in the algorithm
                select_comp += 1
                if sorted_arr_select[min_elm] > sorted_arr_select[j]:
                    min_elm = j
            # Swapping the minimum value with the array first element.
            sorted_arr_select[i], sorted_arr_select[min_elm] = sorted_arr_select[min_elm], sorted_arr_select[i]

        # Returning the sorted array and its total number of comparisons.
        return sorted_arr_select, select_comp

    @timed
    def insertion_sort(self):
        sorted_arr_insert = self.Arr.copy()
        insert_comp = 0
        for i in range(self.arrLen - 1):
            tmp = sorted_arr_insert[i]
            j = i
            insert_comp += 1
            while j > 0 and tmp < sorted_arr_insert[j - 1]:
                insert_comp += 1
                sorted_arr_insert[j] = sorted_arr_insert[j - 1]
                j -= 1
            sorted_arr_insert[j] = tmp
        return sorted_arr_insert, insert_comp

    def heap_sort(self):
        def heapify(arr, n, itr):
            count = 0
            largest = itr
            l = 2 * itr + 1
            r = 2 * itr + 2
            if l < n and arr[itr] < arr[l]:
                largest = l
            if r < n and arr[largest] < arr[r]:
                largest = r
            if largest != itr:
                count += 1
                arr[itr], arr[largest] = arr[largest], arr[itr]
                count += heapify(arr, n, largest)
            return count

        heap_comp = 0
        sorted_arr_heap = self.Arr.copy()
        for i in range(self.arrLen, -1, -1):
            heapify(sorted_arr_heap, self.arrLen, i)
            heap_comp += heapify(sorted_arr_heap, i, 0)
        for i in range(self.arrLen - 1, 0, -1):
            sorted_arr_heap[i], sorted_arr_heap[0] = sorted_arr_heap[0], sorted_arr_heap[i]
            heap_comp += heapify(sorted_arr_heap, i, 0)
        return sorted_arr_heap, heap_comp

    @timed
    def merge_sort(self):
        input_array = self.Arr.copy()
        return SortingAlgo.merge_sort_real(input_array)

    @staticmethod
    def merge_sort_real(sorted_arr_merge):
        num_comp = 0

        if len(sorted_arr_merge) <= 1:
            return sorted_arr_merge, num_comp

        left_arr = SortingAlgo.merge_sort_real(sorted_arr_merge[:len(sorted_arr_merge) // 2])
        right_arr = SortingAlgo.merge_sort_real(sorted_arr_merge[len(left_arr[0]):])

        num_comp += left_arr[1] + right_arr[1]

        left_index = 0
        right_index = 0
        final_index = 0

        while left_index < len(left_arr[0]) and right_index < len(right_arr[0]):
            num_comp += 1
            if left_arr[0][left_index] < right_arr[0][right_index]:
                sorted_arr_merge[final_index] = left_arr[0][left_index]
                left_index += 1
            else:
                sorted_arr_merge[final_index] = right_arr[0][right_index]
                right_index += 1
            final_index += 1

        while left_index < len(left_arr[0]):
            sorted_arr_merge[final_index] = left_arr[0][left_index]
            left_index += 1
            final_index += 1
            num_comp += 1

        while right_index < len(right_arr[0]):
            sorted_arr_merge[final_index] = right_arr[0][right_index]
            right_index += 1
            final_index += 1
            num_comp += 1

        return sorted_arr_merge, num_comp

    @staticmethod
    def quick_sort_2(arr,count):
        if len(arr) < 2:
            return arr
        else:
            pivot = arr[0]
            count = 21
            less = [i for i in arr[1:] if i <= pivot]
            greater = [i for i in arr[1:] if i > pivot]
            return SortingAlgo.quick_sort_2(less, count) + [pivot] + SortingAlgo.quick_sort_2(greater, count)

    '''The running time of this function, would not be exactly correct since it has to call the staticmethod above.'''
    @timed
    def quick_sort(self):
        count = 0
        return SortingAlgo.quick_sort_2(self.Arr, count)


UserArr = [1, 2, 3, 55, 5, 6, 8, 7, 9, 111]
sortAlgos = SortingAlgo(UserArr)
# [1, 2, 3, 55, 5, 6, 8, 7, 1, 111]
FinalArr = UserArr
# SortedArr = sortAlgos.bubble_sort(UserArr)
# select_sorted, select_comp = sortAlgos.selection_sort()
# SortedArr, comparisons = sortAlgos.insertion_sort()
# MergeArr, merge_comp = sortAlgos.merge_sort()

# InsertArr, insert_comp = sortAlgos.insertion_sort()
QuickArr = sortAlgos.quick_sort()
print(QuickArr)
# print(Count)
# print(heap_comp, merge_comp, insert_comp)
# print(insert_comp, heap_comp, merge_comp)
# print(InsertArr, HeapArr, MergeArr)

#
# SortedArr = bubble_sort(FinalArr)
# print(FinalArr)
# SortedArr, comparisons = insertion_sort(FinalArr)
# print(comparisons)
