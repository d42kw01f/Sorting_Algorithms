import random
import time


class SortingAlgo:
    __slots__ = ['Arr', 'arrLen', 'arrMax', 'arrMin']

    def __init__(self, lst):
        self.Arr = lst
        self.arrLen = len(self.Arr)
        self.arrMax = max(self.Arr)
        self.arrMin = min(self.Arr)

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
        num_comp = 0
        for i in range(self.arrLen):
            min_val = i
            for j in range(i, self.arrLen):
                num_comp += 1
                if self.Arr[j] < self.Arr[min_val]:
                    min_val = j
            temp = self.Arr[i]
            self.Arr[i] = self.Arr[min_val]
            self.Arr[min_val] = temp
        return self.Arr

    @timed
    def insertion_sort(self):
        srted_arr = [None] * self.arrLen
        for i in range(self.arrLen):
            tmp = self.Arr[i]
            j = i
            while j > 0 and tmp < self.Arr[j - 1]:
                self.Arr[j] = self.Arr[j - 1]
                j -= 1
            srted_arr[j] = tmp
        return srted_arr

    @timed
    def merge_sort(self):
        def merge_sort_helper(lyst, buffer, low, high):
            if low < high:
                middle = (low + high) // 2

                merge_sort_helper(lyst, buffer, low, middle)
                merge_sort_helper(lyst, buffer, middle + 1, high)
                merge(lyst, buffer, low, middle, high)

        def merge(lyst, buffer, low, middle, high):
            i1 = low
            i2 = middle + 1

            for i in range(low, high + 1):
                if i1 > middle:
                    buffer[i] = lyst[i2]  # 1st sublist exhausted
                    i2 += 1
                elif i2 > high:
                    buffer[i] = lyst[i1]  # 2nd sublist exhausted
                    i1 += 1
                elif lyst[i1] < lyst[i2]:
                    buffer[i] = lyst[i1]  # item in 1st sublist
                    i1 += 1
                else:
                    buffer[i] = lyst[i2]  # item in 2nd sublist
                    i2 += 1
            for i in range(low, high + 1):  # copy sorted items back to
                lyst[i] = buffer[i]

        copy_buffer = [None] * self.arrLen
        merge_sort_helper(self.Arr, copy_buffer, 0, self.arrLen - 1)
        return copy_buffer

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

    '''The running time for this function, would not be exactly correct since it has to call the staticmethod above.'''
    @timed
    def quick_sort(self):
        return self.quick_sort_2(self.Arr)

    @timed
    def bubble_sort(self):
        # Start to sorting the self.Array.
        for i in range(self.arrLen - 1):
            # Check if the self.Array sorted.
            # This will allow the programs to figure out whether the Array is already sorted later.
            is_arr_sorted = False
            for j in range(self.arrLen - 1 - i):
                if self.Arr[j] > self.Arr[j + 1]:
                    self.Arr[j], self.Arr[j + 1] = self.Arr[j + 1], self.Arr[j]
                    # If the self.Array sorted return True
                    is_arr_sorted = True

            # If the self.Array is per-sorted, then break the loop.
            if not is_arr_sorted:
                break
        return self.Arr

    @timed
    def count_sort(self):
        # First check if the given array is null
        if not self.Arr:
            return []

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
        return sorted_arr

    @timed
    def heap_sort(self):
        def heapify(arr, n, itr):
            max_elem, left, right = itr, 2 * itr + 1, 2 * itr + 2
            # if the left element is greater than root
            if left <= n and arr[left] > arr[max_elem]:
                max_elem = left
            # if the right element is greater than root
            if right <= n and arr[right] > arr[max_elem]:
                max_elem = right

            # if the max is not i
            if max_elem != itr:
                arr[itr], arr[max_elem] = arr[max_elem], arr[itr]
                heapify(arr, n, max_elem)

        for i in range(self.arrLen // 2, -1, -1):
            heapify(self.Arr, self.arrLen - 1, i)

        for i in range(self.arrLen - 1, -1, -1):
            # swap last element of the max-heap with the first element
            self.Arr[i], self.Arr[0] = self.Arr[0], self.Arr[i]

            # exclude the last element from the heap and rebuild the heap
            heapify(self.Arr, i - 1, 0)
        return self.Arr


def user_menu(user_choice):
    # ArrElem = int(input('Number of Elements in the Array: '))
    if user_choice == 1:
        arr_elem = int(input('Number of Elements in the Array: '))
        return [round(random.uniform(-1000000, 1000000)) for _ in range(arr_elem)]
    elif user_choice == 2:
        try:
            arr_elem = int(input('Number of Elements in the Array: '))
            return [int(input(f"Enter Elem {ArrNum}: ")) for ArrNum in range(arr_elem)]
        except TypeError:
            print('Oops! Some algorithms do not work with str, Thus please enter int only.')

    else:
        exit()


if __name__ == '__main__':
    while True:
        print("""
        First Let's Create a self.Array Shall we:
            1. Randomly Generated Array
            2. Enter an Array Manually
            3. Exit
        """)

        UserChoice = int(input("Enter your option: "))
        if not type(UserChoice) is int:
            raise TypeError("Enter the right number")
        UserArr = user_menu(UserChoice)
        print('The Array is --> {}'.format(UserArr))

        # Check if the Array is empty
        if not UserArr:
            print('Looks like the Array is empty')
            exit()

        print("\n\t\tSorting started...\n")
        # Initializing an instance
        SortArr = SortingAlgo(UserArr)

        TheArrayHeap = SortArr.heap_sort()
        print(TheArrayHeap)

        # Running the Selection sort algorithm
        TheArraySelection = SortArr.selection_sort()
        # print("Selection Sorted Array: {}".format(TheArraySelection))

        # Running the Merge Sort Algorithm
        TheArrayMarge = SortArr.merge_sort()
        # print("Marge Sorted Array {}".format(TheArrayMarge))

        # Running the Insertion Sort Algorithm
        TheArrayInsertion = SortArr.insertion_sort()
        # print("Insertion Sorted Array: {}".format(TheArrayInsertion))

        # Running the bubble sort algorithm
        TheArrayBubble = SortArr.bubble_sort()
        # print("Bubble Sorted Array: {}".format(TheArrayBubble))

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
