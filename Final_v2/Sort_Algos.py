import time
import random
from pathlib import Path
import pandas as pd
import csv
import os


class SortingAlgo:

    __slots__ = ['Arr', 'arrLen', 'arrMax', 'arrMin', 'num_comp']

    def __init__(self, arr_lst):
        self.Arr = arr_lst
        self.arrLen = len(arr_lst)
        self.arrMax = max(arr_lst)
        self.arrMin = min(arr_lst)

    # This function allows to measure each algorithm runtime
    @staticmethod
    def timed(f):
        def _timed(*args, **kwargs):
            function_name = f.__name__
            start = time.time()
            v = f(*args, **kwargs)
            run_time = round((time.time() - start)*1000.0, 4)
            print("===" * 50)
            print(f"--> Running Time of {function_name} Algorithm is: {str(run_time)} ms")
            SortingAlgo._write_csv(function_name, v, run_time)
            final_v = (v, run_time)
            return final_v

        return _timed

    @staticmethod
    def _write_csv(func_name, comparisons, running_time):
        the_file = Path('sorting_algorithms_output_10519381.csv')
        numbers_comparisons = comparisons[1]
        len_arr = len(comparisons[0])
        if not the_file.is_file():
            header = ['Sorting Algorith Name', 'Array Length', 'Num. of Comparisons', 'Run Time']
            with open(the_file, 'w', encoding='utf-8') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(header)
        data_frame = pd.DataFrame({'Sorting Algorith Name': [func_name], 'Array Length': [len_arr], 'Num. of Comparisons': [numbers_comparisons], 'Run Time': [running_time]})
        print(data_frame)
        data_frame.to_csv(the_file, mode='a', header=False, index=False)

    @timed
    def selection_sort(self):
        num_comp = 0
        # Travelling through all the elements in the given array
        sorted_arr = self.Arr.copy()
        for i in range(self.arrLen):
            # bellow codes will allow to find the minimum element in the array
            min_elm = i
            for j in range(i + 1, self.arrLen):
                # Following code allows find total number of comparisons, made in the algorithm
                num_comp += 1
                if sorted_arr[min_elm] > sorted_arr[j]:
                    min_elm = j
            # Swapping the minimum value with the array first element.
            sorted_arr[i], sorted_arr[min_elm] = sorted_arr[min_elm], sorted_arr[i]

        # Returning the sorted array and its total number of comparisons.
        return sorted_arr, num_comp

    @timed
    def insertion_sort(self):
        sorted_arr = self.Arr.copy()
        num_comp = 0
        for i in range(self.arrLen):
            tmp = sorted_arr[i]
            j = i
            num_comp += 1
            while j > 0 and tmp < sorted_arr[j - 1]:
                num_comp += 1
                sorted_arr[j] = sorted_arr[j - 1]
                j -= 1
            sorted_arr[j] = tmp
        return sorted_arr, num_comp

    @staticmethod
    def _mergesort(sorted_arr):
        num_comp = 0

        if len(sorted_arr) <= 1:
            return sorted_arr, num_comp

        left_arr = SortingAlgo._mergesort(sorted_arr[:len(sorted_arr) // 2])
        right_arr = SortingAlgo._mergesort(sorted_arr[len(left_arr[0]):])

        num_comp += left_arr[1] + right_arr[1]

        left_index = 0
        right_index = 0
        final_index = 0

        while left_index < len(left_arr[0]) and right_index < len(right_arr[0]):
            num_comp += 1
            if left_arr[0][left_index] < right_arr[0][right_index]:
                sorted_arr[final_index] = left_arr[0][left_index]
                left_index += 1
            else:
                sorted_arr[final_index] = right_arr[0][right_index]
                right_index += 1
            final_index += 1

        while left_index < len(left_arr[0]):
            sorted_arr[final_index] = left_arr[0][left_index]
            left_index += 1
            final_index += 1
            num_comp += 1

        while right_index < len(right_arr[0]):
            sorted_arr[final_index] = right_arr[0][right_index]
            right_index += 1
            final_index += 1
            num_comp += 1

        return sorted_arr, num_comp

    @timed
    def merge_sort(self):
        input_array = self.Arr.copy()
        return SortingAlgo._mergesort(input_array)

    @staticmethod
    def _quicksort(arr, left_arr, right_arr):
        def partition(arr, left_arr, right_arr):
            i = left_arr + 1
            pivot = arr[left_arr]
            j = i + 1
            for j in range(left_arr + 1, right_arr + 1):
                if arr[j] < pivot:
                    arr[j], arr[i] = arr[i], arr[j]
                    i += 1
            pos = i - 1
            arr[left_arr], arr[pos] = arr[pos], arr[left_arr]
            return pos

        if left_arr < right_arr:
            place = partition(arr, left_arr, right_arr)
            SortingAlgo._quicksort(arr, left_arr, place - 1)
            SortingAlgo._quicksort(arr, place + 1, right_arr)
            comparison = right_arr - left_arr
            num_comp = +comparison
            return arr, num_comp

    @timed
    def quick_sort(self):
        sorted_arr = self.Arr.copy()
        arr_left = 0
        arr_right = self.arrLen - 1
        sorted_arr, total_comp = SortingAlgo._quicksort(sorted_arr, arr_left, arr_right)
        return sorted_arr, total_comp

    @timed
    def bubble_sort(self):
        num_comp = 0
        sorted_arr = self.Arr
        # Start to sorting the self.Array.
        for i in range(self.arrLen - 1):
            # Check if the self.Array sorted.

            for j in range(self.arrLen - 1 - i):
                num_comp += 1
                if sorted_arr[j] > sorted_arr[j + 1]:
                    sorted_arr[j], sorted_arr[j + 1] = sorted_arr[j + 1], sorted_arr[j]
                    # If the self.Array sorted return True
                    is_arr_sorted = True
        return sorted_arr, num_comp

    @timed
    def optimal_bubble_sort(self):
        num_comp = 0
        sorted_arr = self.Arr
        # Start to sorting the self.Array.
        for i in range(self.arrLen - 1):
            # Check if the self.Array sorted.
            # This will allow the programs to figure out whether the Array is already sorted later.
            is_arr_sorted = False
            for j in range(self.arrLen - 1 - i):
                num_comp += 1
                if sorted_arr[j] > sorted_arr[j + 1]:
                    sorted_arr[j], sorted_arr[j + 1] = sorted_arr[j + 1], sorted_arr[j]
                    # If the self.Array sorted return True
                    is_arr_sorted = True

            # If the self.Array is per-sorted, then break the loop.
            if not is_arr_sorted:
                break
        return sorted_arr, num_comp

    @timed
    def count_sort(self):
        auxi_arr = [0] * self.arrLen
        sorted_arr = self.Arr.copy()
        num_comp = 0

        for val in sorted_arr:
            num_less_elem = 0
            for elem in sorted_arr:
                num_comp += 1
                if elem < val:
                    num_less_elem += 1
            auxi_arr[num_less_elem] = val

        return auxi_arr, num_comp

    @timed
    def general_count_sort(self):
        # First check if the given array is null
        if not self.Arr:
            return []

        num_comp = 0
        # Get the length of the array
        count_len = self.arrMax + 1 - self.arrMin
        # Create another array from above calculated length
        count = [0] * count_len

        for Val in self.Arr:
            count[Val - self.arrMin] += 1
        for i in range(1, count_len):
            count[i] += count[i - 1]

        # Creating an array to hold sorted elements.
        sorted_arr = [None] * self.arrLen

        for i in reversed(range(0, self.arrLen)):
            sorted_arr[count[self.Arr[i] - self.arrMin] - 1] = self.Arr[i]
            count[self.Arr[i] - self.arrMin] -= 1

        # Returning the sorted array.
        return sorted_arr, num_comp

    @timed
    def heap_sort(self):
        def heapify(arr, n, itr):
            count = 0
            largest = itr
            left = 2 * itr + 1
            right = 2 * itr + 2
            if left < n and arr[itr] < arr[left]:
                largest = left
            if right < n and arr[largest] < arr[right]:
                largest = right
            if largest != itr:
                count += 1
                arr[itr], arr[largest] = arr[largest], arr[itr]
                count += heapify(arr, n, largest)
            return count

        num_comp = 0
        sorted_arr = self.Arr.copy()
        for i in range(self.arrLen, -1, -1):
            heapify(sorted_arr, self.arrLen, i)
            num_comp += heapify(sorted_arr, i, 0)
        for i in range(self.arrLen - 1, 0, -1):
            sorted_arr[i], sorted_arr[0] = sorted_arr[0], sorted_arr[i]
            num_comp += heapify(sorted_arr, i, 0)
        return sorted_arr, num_comp