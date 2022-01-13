import random
import time

def bubble_sort(Arr):
    # Check the Length of the given array
    LenArr = len(Arr)

    # Start to storting the Array.
    for i in range(LenArr-1):
        # Check if the Array sorted. This will allows the programs to figure out whether the Array is already sorted later.
        IsArrSorted = False
        for j in range(LenArr-1-i):
            if Arr[j] > Arr[j+1]:
                Arr[j], Arr[j+1] = Arr[j+1], Arr[j]
                # If the Array softed return True
                IsArrSorted = True
        
        # If the Array is per-storted, then break the loop.
        if not IsArrSorted:
            break
        
    return Arr

def UserMenue(UserChoice):

    ArrElem = int(input('Number of Elements in the Array: '))
    if UserChoice == 1:
        return [round(random.uniform(, 1000000)) for _ in range(ArrElem)]
    elif UserChoice == 2:
        return [input(f"Enter Elem {ArrNum}: ") for ArrNum in range(ArrElem)]
    else:
        exit()

if __name__ == '__main__':
    print("""
    First Let's Create a Array Shall we:
        1. Randomly Generated Array
        2. Enter an Array Manually
        3. Exit
    """)

    UserChoice = int(input("Enter your option: "))
    if not type(UserChoice) is int:
        raise TypeError("Enter the right number")
    UserArr = UserMenue(UserChoice)
    print('The Array is --> {}'.format(UserArr))

    # # UserArr = ['123', '2313', '3412412', '12']
    # UserArr = [1, 2, 3, 4]
    # UserArr = [801889, 968011, 562363, 953134, 85356, 308539, 104232, 666504, 42130, 621394, 71463, 327225, 873066, 234777, 115901, 812591, 253243, 887371, 598509, 255978]

    print("\n\t\tSorting started...\n")
    start_time = time.time()
    TheArray = bubble_sort(UserArr)
    final_time = time.time() - start_time
    print("Sorted Array: {}".format(TheArray))
    print("\n\n--- %s seconds ---" % (final_time))


