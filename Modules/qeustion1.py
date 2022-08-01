TheData = [20, 3, 4, 8, 12, 99, 4, 26, 4]

def InsertionSort(TheData):
    for count in range(1, len(TheData)):
        reverseCount = count
        while TheData[count - 1] > TheData[count] and reverseCount > 0:
            TheData[count] , TheData[count - 1] = TheData[count - 1] , TheData[count]
            reverseCount -= 1
    
def PrintArray(TheData):
    for i in range(len(TheData)):
        print(TheData[i])

InsertionSort(TheData)
PrintArray(TheData)