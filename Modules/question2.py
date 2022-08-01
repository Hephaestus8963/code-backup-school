class HiddenBox:
    #__BoxName String
    #__CreatorName String
    #__GameLocation String
    #__DateHidden String
    #__LastFoundBy [10] [2] String
    #__IsActive Boolean

    def __init__(self, BoxName, CreatorName, DateHidden, GameLocation):
        self.__BoxName = BoxName
        self.__CreatorName = CreatorName
        self.__DateHidden = DateHidden
        self.__GameLocation = GameLocation
        self.__IsActive = False
        self.__LastFoundBy = [["" for j in range(0, 10)] for i in range(0, 2)] 

    def GetBoxName():
        return self.__BoxName
    
    def GetGameLocation():
        return self.__GameLocation
    

class PuzzleBox(HiddenBox):
    #__PuzzleText String
    #__Solution String

    def __init__(self, BoxName, CreatorName, DateHidden, GameLocation):
        super().__init__(BoxName, CreatorName, DateHidden, GameLocation)
        self.__PuzzleText = PuzzleText
        self.__Solution = Solution




TheBoxes = [HiddenBox("", "", "", "") for i in range(0, 10000)]

def NewBox(TheBoxes, BoxNum):
    NewBoxName = input("Enter name of new box: ")
    NewCreatorName = input("Enter new creator name: ")
    NewDateHidden = input("Enter new date hidden: ")
    NewGameLocation = input("Enter new game location for box: ")
    TheBoxes[BoxNum] = HiddenBox(NewBoxName, NewCreatorName, NewDateHidden, NewGameLocation)
    return BoxNum + 1

NumBoxes = 0
NumBoxes = NewBox(TheBoxes, NumBoxes)