QueueData = ["" for i in range(20)]
FirstPos = 0
LastPos = 0

def Enqueue(item):
    if LastPos >= 19:
        return False    
    else:
        global LastPos
        QueueData[LastPos + 1] = item
        LastPos += 1
        return True

def ReadFile(FileName):
    try:
        file = open(FileName)
        for line in file:
            if Enqueue(line):
                return 2
            else:
                return 1
    except:
        return -1

def Remove():
    if LastPos < 2:
        return "No Items"
    
    first,second = QueueData[FirstPos], QueueData[FirstPos + 1]
    QueueData[FirstPos], QueueData[FirstPos + 1] = ""
    return (first + "" + second)

FileToRead = ""
while FileToRead != "Stop":
    FileToRead = input("Enter File Name: ")
    ProcessReturns = ReadFile(FileToRead)
    if ProcessReturns == -1:
        print("Text file could not be found.")
    elif ProcessReturns == 1:
        print("THe queue is full.")
    elif ProcessReturns == 2:
        print("All items were successfully added to queue.")
