#region Bubble Sort Algorithm
def BubbleSort(arr):
    swap = True
    # The swap variable keeps track of whether or not any elements in the array were swaped. 
    # If the swap variable is false at the end of the array, no elements were swapped because the list is sorted.
    while swap == True:
        swap = False
        # We reset swap to false because at the start of the array, we haven't swapped any variables.
        n = 1
        # n is the number of values that have already been sorted i.e. how many elements have bubbled up
        # It is initialised as 1 because at the start we have len(arr) - 1 elements at the start
        # initialising it with 0 and subtracting it from len(arr) along with 1 is the same
        for i in range(len(arr) - n):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i+1] = arr[i+1], arr[i] #Swapping elements
                swap = True
        
        n += 1
        # If the swap variable is true here this means the list has shuffled elements and needs to be checked again.
        # If not, the list has no shuffled elements and so the list is sorted.
# endrgion

#region Insertion Sort Algorithm
def InsertionSort(arr):
    for i in range(1, len(arr)):
        # We check through each and every element in the array, starting from the second element, ...
        j = i
        # ... while keeping track of where we are
        while arr[j] < arr[j - 1] and j > 0:
            # If the element we are currently on is less than the previous element, we keep on pushing the element until it is no longer smaller.
            # We do it until we reach the start of the array
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1
# endregion

#region [Needs Attention] Quick Sort Algorithm
def QuickSort(arr):
    pass
#endregion
