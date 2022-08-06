from queue import Queue

QueueData = Queue(20)
First = 0
Last = QueueData.qsize()

for i in range(10): QueueData.put(i)

def Enqueue(item):
    if QueueData.empty(): return False
    
    global Last
    QueueData.put(item)
    Last += 1
    return True

def ReadFile(FileName):
    try:
        file = open(FileName)
        line = file.readline()
        if Enqueue(line):
            return 2
        else:
            return 1
    except:
        return -1

def Remove():
    if Last < 2:
        return "No Items"
    
    first = QueueData.get()
    second = QueueData.get()
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
