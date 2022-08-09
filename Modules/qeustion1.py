TheData = [20, 3, 4, 8, 12, 99, 4, 26, 4]

def InsertionSort(arr):
    for i in range(0, len(arr)):
        j = i
        while arr[j] < arr[j-1] and j > 0:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1
    
def PrintArray(arr):
    for i in range(len(arr)):
        print(arr[i])

def LinearSearch(arr):
    item = int(input("Enter number: "))
    found = False
    count = 0
    while count < len(arr) and not found:
        if item == arr[count]:
            print("Found")
            found = True
            return found
        
        count += 1
    
    print("Not found")
    return found
    
LinearSearch(TheData)