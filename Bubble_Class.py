import random
import time

class SortingAlgo():

    __slots__ = ['Arr', 'LenArr']

    def __init__(self, Arr):
        self.Arr = Arr
        # Getting the Lenght of the Array
        self.LenArr = len(self.Arr)

    def bubble_sort(self):
        
        # Start to storting the self.Array.
        for i in range(self.LenArr-1):
            # Check if the self.Array sorted. This will allows the programs to figure out whether the Array is already sorted later.
            IsArrSorted = False
            for j in range(self.LenArr-1-i):
                if self.Arr[j] > self.Arr[j+1]:
                    self.Arr[j], self.Arr[j+1] = self.Arr[j+1], self.Arr[j]
                    # If the self.Array softed return True
                    IsArrSorted = True
            
            # If the self.Array is per-storted, then break the loop.
            if not IsArrSorted:
                break
            
        return self.Arr

def UserMenue(UserChoice):

    ArrElem = int(input('Number of Elements in the Array: '))
    if UserChoice == 1:
        return [round(random.uniform(-1000000, 1000000)) for _ in range(ArrElem)]
    elif UserChoice == 2:
        return [input(f"Enter Elem {ArrNum}: ") for ArrNum in range(ArrElem)]
    else:
        exit()

if __name__ == '__main__':
    print("""
    First Let's Create a self.Array Shall we:
        1. Randomly Generated self.Array
        2. Enter an self.Array Manually
        3. Exit
    """)

    UserChoice = int(input("Enter your option: "))
    if not type(UserChoice) is int:
        raise TypeError("Enter the right number")
    UserArr = UserMenue(UserChoice)
    print('The self.Array is --> {}'.format(UserArr))

    print("\n\t\tSorting started...\n")
    start_time = time.time()
    SortArr = SortingAlgo(UserArr)
    TheArray = SortArr.bubble_sort()
    final_time = time.time() - start_time
    print("Sorted self.Array: {}".format(TheArray))
    print("\n\n--- %s seconds ---" % (final_time))


