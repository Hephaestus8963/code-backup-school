Emoves = ["ThunderBolt", "Electro Ball", "Quick Attack", "Thunder", "Thunder ball"]

import random

class Pokemon:

    def __init__(self, name:str, type:str, hpIncrementRatio:float = 2.0, hp:int = 8, level:int = 1) -> None:
        self.hp = hp
        self.name = name
        self.level = level
        self.MAXMOVES = 4
        self.type = type
        self.hpIncementRatio = hpIncrementRatio
        self.moves = []
    
    def _LevelUp(self, NewMove:str = ""):
        self.level += 1
        self.hp += self.hp * self.hpIncementRatio
        print("{} leveled up to level {}. His stats:\nHitpoints: {}".format(self.name, self.level, self.hp))
        if NewMove == "" or NewMove in self.moves: return
        elif len(self.moves) < self.MAXMOVES:
            print("{} learned a new move: {}".format(self.name, NewMove))
            self.moves.append(NewMove)
        elif len(self.moves) > self.MAXMOVES:
            print("{} is trying to learn {} but can not learn more than {} moves.\n".format(self.name, NewMove, self.MAXMOVES))
            choice = ""
            while choice != 'y' or choice != 'n':
                choice = input("Make him delete one move? (y/n) : ")
            if choice == 'n':
                print("{} did not learn {}.".format(self.name, NewMove))
            elif choice == 'y':
                choice = ""
                while choice < "1" and choice > "4":
                    for i in range(1, len(self.moves)):
                        print("{}. {}".format(i, self.moves[i-1]))
                    choice = ("Which move would you like to delete? ")
                
                self.moves[int(choice)] = NewMove
        

class Pickachu(Pokemon):

    def __init__(self, name = "Pickachu") -> None:
        super().__init__(name = name,type = "Electric", hpIncrementRatio=.5)
        self._call = "Pika!"
        self._feedCounter = 0
    
    def feed(self):
        print("Fed {}, he is happy. He says {}".format(self.name, self._call))
        self._feedCounter += 1
        if self._feedCounter >= 5:
            self._feedCounter = 0
            self._LevelUp(random.choice(Emoves))


