arr = [25, 28, 13, 35, 50]
#Goal: find the third largest value of the array.

def FindThirdLargest(arr):

    # This function works by constantly updating first, second and third variable
    # while going though a normal highest value finding algorithm

    # First keeps track of the highest value normally
    # Seoncd keeps track of the previous value of first
    # Third keep track of the previoud value of second
    
    first = -1
    second = -1 # Lowest value posible
    third = -1 #Lowest value possible
    for i in range(1, len(arr)):

        # This is a normal highest finding condition
        # this is done until first is the maximum value
        if arr[i] > first:
            third = second
            second = first
            first = arr[i]

        # If the above statement is not true, first is the maximum value
        # so now we try find the max value of second.
        # we redo the highest function for just the second variable
        elif arr[i] > second:
            third = second
            second = arr[i]

        # If the above statement is not true, second is now the second max value
        # so the maximum value excluding first and second is the third maximum value
        # so we repeat for third
        elif arr[i] > third:
            third  = arr[i]

    print(third)
    

FindThirdLargest(arr)