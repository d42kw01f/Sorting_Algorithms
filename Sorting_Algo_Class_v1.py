import random
import time
from tqdm.auto import tqdm

class SortingAlgo:

    __slots__ = ['Arr', 'arrLen', 'arrMax', 'arrMin']

    def __init__(self, Arr):
        self.Arr = Arr
        self.arrLen = len(self.Arr)
        self.arrMax = max(self.Arr)
        self.arrMin = min(self.Arr)
    
    # This function allows to measure the each algorithm runtime
    def timed(f):
        def _timed(*args, **kwargs):
            start = time.time()
            v = f(*args, **kwargs)
            theTime = time.time() - start
            print("---"*50)
            print(f"\nRunning Time of {f.__name__} Algorithm is: {str(theTime)}")
            return v
        return _timed
    
    @timed
    def selection_sort(self):
        numComp = 0
        for i in range(self.arrLen):
            minVal = i
            for j in range(i, self.arrLen):
                numComp += 1
                if self.Arr[j] < self.Arr[minVal]:
                    minVal = j
            temp = self.Arr[i]
            self.Arr[i] = self.Arr[minVal]
            self.Arr[minVal] = temp
        return self.Arr

    @timed
    def bubble_sort(self):
        # Start to storting the self.Array.
        for i in range(self.arrLen-1):
            # Check if the self.Array sorted. This will allows the programs to figure out whether the Array is already sorted later.
            IsArrSorted = False
            for j in range(self.arrLen-1-i):
                if self.Arr[j] > self.Arr[j+1]:
                    self.Arr[j], self.Arr[j+1] = self.Arr[j+1], self.Arr[j]
                    # If the self.Array softed return True
                    IsArrSorted = True
            
            # If the self.Array is per-storted, then break the loop.
            if not IsArrSorted:
                break
            
        return self.Arr

    @timed
    def count_sort_int(self):
        # First check if the given array is null
        if self.Arr == []:
            return []

        # Get the length of the array
        CountLen = self.arrMax + 1 - self.arrMin
        # Create a another array from above calculated length
        Count = [0] * CountLen

        for Val in self.Arr: Count[Val - self.arrMin] += 1
        for i in range(1, CountLen): Count[i] = Count[i] + Count[i-1]

        # Creating an array to hold sorted elements. 
        SortedArr = [0] * self.arrLen

        for i in reversed(range(0, self.arrLen)):
            SortedArr[Count[self.Arr[i]-self.arrMin]-1] = self.Arr[i]
            Count[self.Arr[i]-self.arrMin] -= 1

        # Finally returning the sorted array.
        return SortedArr


def UserMenue(UserChoice):

    # ArrElem = int(input('Number of Elements in the Array: '))
    if UserChoice == 1:
        ArrElem = int(input('Number of Elements in the Array: '))
        return [round(random.uniform(-1000000, 1000000)) for _ in range(ArrElem)]
    elif UserChoice == 2:
        try:
            ArrElem = int(input('Number of Elements in the Array: '))
            return [int(input(f"Enter Elem {ArrNum}: ")) for ArrNum in range(ArrElem)]
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
        UserArr = UserMenue(UserChoice)
        print('The Array is --> {}'.format(UserArr))

        # Check if the Array is empty
        if UserArr == []:
            print('Looks like the Array is empty')
            exit()

        print("\n\t\tSorting started...\n")
        # Initializing an instance
        SortArr = SortingAlgo(UserArr)

        # Running the bubble sort algorithm
        TheArraySelection = SortArr.selection_sort()
        print("Selection Sorted Array: {}".format(TheArraySelection))

        # Running the bubble sort algorithm
        TheArrayBubble = SortArr.bubble_sort()
        print("Bubble Sorted Array: {}".format(TheArrayBubble))

        # Running the Count Sort Algorithm
        TheArrayCount = SortArr.count_sort_int()
        print("Count Sorted Array: {}".format(TheArrayCount))

        # Checking all the Array are equal to each other
        if TheArrayBubble == TheArraySelection == TheArrayCount:
            print("\n\n-----> Every Array equal to each other")
        else:
            print('Hmm Something went wrong!!!')
        input("\n\n\tPress Any Key to continue: ")
        print('\n\n')
