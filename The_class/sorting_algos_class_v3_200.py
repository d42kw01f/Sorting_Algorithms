import time
import random
from pathlib import Path
import pandas as pd
import csv


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
            run_time = round((time.time() - start) * 1000.0, 4)
            print("===" * 50)
            print(f"--> Running Time of {function_name} Algorithm is: {str(run_time)} ms")
            v['Run Time'] = run_time
            SortingAlgo.write_csv(function_name, v)

            return v

        return _timed

    @staticmethod
    def write_csv(func_name, result_dic):
        the_file = Path('sorting_algorithms_output_10519381.csv')
        numbers_comparisons = result_dic['comparisons']
        len_arr = len(result_dic['sorted array'])
        running_time = result_dic['Run Time']
        if not the_file.is_file():
            header = ['Sorting Algorith Name', 'Array Length', 'Num. of Comparisons', 'Run Time']
            with open(the_file, 'w', encoding='utf-8') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(header)
        data_frame = pd.DataFrame({'Sorting Algorith Name': [func_name], 'Array Length': [len_arr],
                                   'Num. of Comparisons': [numbers_comparisons], 'Run Time': [running_time]})
        data_frame.to_csv(the_file, mode='a', header=False)

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

        select_results = {'sorted array': sorted_arr,
                          'comparisons': num_comp}

        # Returning the sorted array and its total number of comparisons.
        return select_results

    @timed
    def insertion_sort(self):
        sorted_arr = self.Arr.copy()
        num_comp = 0
        for i in range(self.arrLen - 1):
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
    def merge_sort_real(sorted_arr):
        num_comp = 0

        if len(sorted_arr) <= 1:
            return sorted_arr, num_comp

        left_arr = SortingAlgo.merge_sort_real(sorted_arr[:len(sorted_arr) // 2])
        right_arr = SortingAlgo.merge_sort_real(sorted_arr[len(left_arr[0]):])

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
        return SortingAlgo.merge_sort_real(input_array)

    '''This is another very easy way of writing quick_sort_2 algorithm. However, 
    I faced few issues when I tried to calculate the running time.
    Since, it has recursive functions in it. Thus, every time the quick_sort_2 function is called
    @timed decorator will also be ran. I wasn't yet good enough figured this issue out. 
    Nonetheless, this is a staticmethod and it can be accessed outside the class.'''

    @staticmethod
    def quick_sort_2(arr):
        if len(arr) < 2:
            return arr
        else:
            pivot = arr[0]
            less = [i for i in arr[1:] if i <= pivot]
            greater = [i for i in arr[1:] if i > pivot]
            return SortingAlgo.quick_sort_2(less) + [pivot] + SortingAlgo.quick_sort_2(greater)

    '''The running time of this function, would not be exactly correct since it has to call the staticmethod above.'''

    @timed
    def quick_sort(self):
        return SortingAlgo.quick_sort_2(self.Arr)

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


# def user_menu(user_choice):
#     # ArrElem = int(input('Number of Elements in the Array: '))
#     if user_choice == 1:
#         arr_elem = int(input('Number of Elements in the Array: '))
#         return [round(random.uniform(-1000000, 1000000)) for _ in range(arr_elem)]
#     elif user_choice == 2:
#         try:
#             arr_elem = int(input('Number of Elements in the Array: '))
#             return [int(input(f"Enter Elem {ArrNum}: ")) for ArrNum in range(arr_elem)]
#         except TypeError:
#             print('Oops! Some algorithms do not work with str, Thus please enter int only.')
#
#     else:
#         exit()


if __name__ == '__main__':
    # while True:
    #     print("""
    #     First Let's Create a self.Array Shall we:
    #         1. Randomly Generated Array
    #         2. Enter an Array Manually
    #         3. Exit
    #     """)
    #
    #     UserChoice = int(input("Enter your option: "))
    #     if not type(UserChoice) is int:
    #         raise TypeError("Enter the right number")
    #     UserArr = user_menu(UserChoice)
    #     print('The Array is --> {}'.format(UserArr))
    #
    #     # Check if the Array is empty
    #     if not UserArr:
    #         print('Looks like the Array is empty')
    #         exit()

        print("\n\t\tSorting started...\n")
        UserArr = [1, 2, 3, 55, 5, 6, 8, 7, 9, 111]
        # Initializing an instance
        SortArr = SortingAlgo([1, 2, 3, 55, 5, 6, 8, 7, 9, 111])

        # # Running the Selection sort algorithm

        # print(vars(SortArr))
        return_list,comp = SortArr.count_sort()
        # time = return_list['Run Time']
        # print(type(return_list))
        # print(return_list)
        # print('Selection Sort comparisons: {}'.format(selection_comp))
        # print("Selection Sorted Array: {}".format(TheArraySelection))
        # print('The Time is: {}'.format(time))

        exit()

        # Running the Insertion Sort Algorithm
        print(UserArr)

        # Running the Heap sort algorithm
        TheArrayHeap, Comparisons = SortArr.heap_sort()
        print("Heap Sorted Array: {}".format(TheArrayHeap))
        print(Comparisons)

        TheArrayInsertion, insert_comp = SortArr.insertion_sort()
        print('Insert Sort comparisons: {}'.format(insert_comp))
        print("Insertion Sorted Array: {}".format(TheArrayInsertion))

        # Running the Merge Sort Algorithm
        TheArrayMarge, merge_comp = SortArr.merge_sort()
        # print("Marge Sorted Array {}".format(TheArrayMarge))
        print('Marge Sort comparisons {}'.format(merge_comp))
        print(TheArrayMarge)

        # Running the bubble sort algorithm
        TheArrayBubble, buble_comp = SortArr.bubble_sort()
        print("Bubble Sorted Array: {}".format(TheArrayBubble))
        print(buble_comp)
        exit()
        # Running the Count Sort Algorithm
        TheArrayCount = SortArr.count_sort()
        # print("Count Sorted Array: {}".format(TheArrayCount))

        TheArrayQuick = SortArr.quick_sort()
        # quickSortFunc = SortArr.timed(SortArr.quick_sort(UserArr))

        # Checking all the Array are equal to each other
        if TheArrayBubble == TheArraySelection == TheArrayCount == TheArrayInsertion == TheArrayHeap:
            print("\n\n-----> Every Array equal to each other <-----")
        else:
            print('\n\n-----> Hmm Something went wrong!!! <-----')
        input("\n\n\tPress Any Key to continue: ")
        print('\n\n')
