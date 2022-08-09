
#region Linear Search
def LinearSearch(arr, item):
    # The linear search algorithm goes through the lisr arr,
    # comparing item to each element of arr
    # It starts from the back and goes to the front but the results would be identical vice versa
    arrLength = len(arr) - 1
    while arrLength > -1 and arr[arrLength] != item:
        arrLength -= 1
    if arrLength == -1:
        raise IndexError('Item Not Found')
    
    return arrLength

#endregion

def BinarySearch(arr, item):
    # The algorithm sorts the array in ascending order
    # The sorting algorithm has been left out for testing purposes

    # This version of the algorithm uses indexing to find out the search query
    First = 0
    Last = len(arr)
    Middle = (First + Last) // 2
    # It first finds the middle element of the list and checks if they are equal
    # If they are, we return the middle index

    # [a, b, c, d, e]
    #  ^  ~  ^  ~  ^
    # start, middle, last

    if item < arr[0] or item > arr[-1]:
        raise IndexError('Item too large for list.')


    while item != arr[Middle]:
        if item > arr[Middle]:
            First = Middle
        # If the middle element is smaller than item, we deacrease the list size to the right-hand elements of the array
        
        # let item <- e
        # [a, b, c, d, e]
        #  ~  ~  ^  ^  ^
        # start, middle, last

        # we then reloop through the new array

        elif item < arr[Middle]:
            Last = Middle - 1
        # If the middle element is larger than the item, we deacrease the list size to the left-hand elements of the array

        # let item <- a
        # [a, b, c, d, e]
        #  ^  ^  ^  ~  ~
        # start, middle, last

        # we then reloop through the new array
        if First == Last and item != arr[Middle]:
            raise IndexError('Item not found')
        
        Middle = (First + Last) // 2
        
    # We repeat until middle = item, then return middle
    return Middle
#endregion

#region Binary Search {Recursion}
def RecursiveBinarySearch(arr, item, first, last):

    if last - first == 1:
        if item == arr[last]:
            return last
        elif item == arr[first]:
            return first
        else:
            raise IndexError('Item not found.')
        

    middle = (first + last) // 2

    print(first, last, middle, arr[middle], item)
    if arr[middle] < item:
        middle = RecursiveBinarySearch(arr, item , middle, last)
    elif arr[middle] > item:
        middle = RecursiveBinarySearch(arr, item, first, middle)

    return middle
#endregion
