import math

class EulerAngle:

    def Rad2Deg() -> float:
        return 180/math.pi

    def Deg2Rad() -> float:
        return math.pi/180

    def __init__(self, rotationInDegrees = None, rotationInRadians = None) -> None:
        if rotationInDegrees == None:
            self.radians = rotationInRadians
            self.degrees = self.radians * EulerAngle.Rad2Deg()
        elif rotationInRadians == None:
            self.degrees = rotationInDegrees
            self.radians = self.degrees * EulerAngle.Deg2Rad()
    
    def __repr__(self) -> str:
        return (str(self.degrees) + "° from center")
    
    def __int__(self) -> int:
        return int(self.degrees)


class Point2D:

    def __init__(self, posX, posY) -> None:
        self.x, self.y = posX, posY
    
    def empty():
        return Point2D(None, None)
    
    def origin():
        return Point2D(0, 0)

    
class Line2D:
    
    def __init__(self, startPoint, endPoint) -> None:
        self.end1 = startPoint
        self.end2 = endPoint
    
    def getLength(self) -> float:
        return math.sqrt((((self.end2.y - self.end1.y) ** 2) + ((self.end2.x-self.end1.x) ** 2)))
    
    def getGradient(self) -> float:
        return (self.end2.y-self.end1.y)/(self.end2.x - self.end1.x)
    
    def getYIntercept(self) -> int:
        return -(self.end1.x * self.getGradient()) + self.end1.y
    
    def Equation(self) -> str:
        return ("y = {}x + {}".format(self.getGradient(), self.getYIntercept()))

class Vector2D:
    
    def __init__(self, startPoint = Point2D.empty(), endPoint = Point2D.empty(), run = None, rise = None) -> None:
        if rise == None and run == None:
            run = (endPoint.x - startPoint.x)
            rise = (endPoint.y - startPoint.y)
        elif startPoint == Point2D.empty() and endPoint == Point2D.empty:
            pass

        
        self.x = run
        self.y = rise
    
    def __repr__(self) -> str:
        return "({}, {})".format(self.x, self.y)
    
    def getMagnitude(self) -> float:
        return math.sqrt(self.y ** 2 + self.x ** 2)
    
    def getDirectionFromCenter(self) -> EulerAngle:
        return EulerAngle(math.atan2(self.y, self.x) * EulerAngle.Rad2Deg())

    def normalized(self):
        Magnitude = self.getMagnitude()
        return Vector2D(run = self.x/Magnitude, rise = self.y/Magnitude)

    def __add__(self, VectorO):
        return Vector2D(run = self.x + VectorO.x, rise = self.y + VectorO.y)
    
    def __sub__(self, VectorO):
        return Vector2D(run = self.x - VectorO.x, rise = self.y - VectorO.y)
    
    def __mul__(self, scaleFactor:int):
        return Vector2D(run = self.x * scaleFactor, rise = self.y * scaleFactor)
    
    def __truediv__(self, scaleFactor:int):
        if scaleFactor == 0:
            raise ValueError("Math error: Divide by zero.")
        
        return Vector2D(run = self.x / scaleFactor, rise = self.y / scaleFactor)
    
    def __eq__(self, VectorO) -> bool:
        return self.x == VectorO.x and self.y == VectorO.y
    
    def __ne__(self, VectorO) -> bool:
        return self.x != VectorO.x and self.y != VectorO.y
    
    def areParallel(self, VectorO) -> bool:
        return int(self.getDirectionFromCenter()) == int(VectorO.getDirectionFromCenter())
    
