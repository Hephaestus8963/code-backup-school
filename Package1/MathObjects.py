import math
from pythonlangutil.overload import Overload 

class EulerAngle:

    def Rad2Deg() -> float:
        return 180/math.pi

    def Deg2Rad() -> float:
        return math.pi/180

    @Overload
    def __init__(self, rotationInDegrees = None, rotationInRadians = None) -> None:
        if rotationInRadians is not None:
            self.radians = rotationInRadians
            self.degrees = self.radians * EulerAngle.Rad2Deg()
        elif rotationInDegrees is not None:
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
    
    def __init__(self, startPoint:Point2D, endPoint:Point2D) -> None:
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
    
    def __init__(self, startPoint:Point2D = None, endPoint:Point2D = None, run:int = None, rise:int = None) -> None:
        if startPoint == None and endPoint == None:
            pass
        elif rise == None and run == None:
            run = (endPoint.x - startPoint.x)
            rise = (endPoint.y - startPoint.y)

        self.x = run
        self.y = rise
    
    def getMagnitude(self) -> float:
        return math.sqrt(self.y ** 2 + self.x ** 2)

    def normalized(self):
        magnitude = self.getMagnitude()
        return self/magnitude

    def getAngularDirection(self) -> EulerAngle:
        return EulerAngle(math.atan2(self.y, self.x) * EulerAngle.Rad2Deg())
    
    def __repr__(self) -> str:
        return "({}, {})".format(self.x, self.y)

    def normalized(self):
        Magnitude = self.getMagnitude()
        return Vector2D(run = self.x/Magnitude, rise = self.y/Magnitude)

    def __add__(self, VectorO):
        return Vector2D(run = self.x + VectorO.x, rise = self.y + VectorO.y)
    
    def __sub__(self, VectorO):
        return Vector2D(run = self.x - VectorO.x, rise = self.y - VectorO.y)
    
    def __mul__(self, obj):
        if type(obj) == int:
            return Vector2D(run = self.x * obj, rise = self.y * obj)
        else:
            raise TypeError("Cannot multiply vector with non-int value.")
    
    def __truediv__(self, scaleFactor:int):
        if scaleFactor == 0:
            raise ValueError("Math error: Divide by zero.")
        
        return Vector2D(run = self.x / scaleFactor, rise = self.y / scaleFactor)
    
    def __eq__(self, VectorO) -> bool:
        return self.x == VectorO.x and self.y == VectorO.y
    
    def __ne__(self, VectorO) -> bool:
        return self.x != VectorO.x and self.y != VectorO.y
    
    def areParallel(self, VectorO) -> bool:
        return (self.x / VectorO.x) == (self. y / VectorO.y)


class Matrix2X2:

    def __init__(self, elemA, elemB, elemC, elemD) -> None:
        self.elemA = elemA
        self.elemB = elemB
        self.elemC = elemC
        self.elemD = elemD
    
    def __add__(self, MatO):
        if type(MatO) == Matrix2X2:
            return Matrix2X2(
                self.elemA + MatO.elemA,
                self.elemB + MatO.elemB,
                self.elemC + MatO.elemC,
                self.elemD + MatO.elemD
            )
        else:
            raise TypeError("Cannot add matrix to non-matrix object.")
    
    def __sub__(self, MatO):
        if type(MatO) == Matrix2X2:
            return Matrix2X2(
                self.elemA - MatO.elemA,
                self.elemB - MatO.elemB,
                self.elemC - MatO.elemC,
                self.elemD - MatO.elemD
            )
        else:
            raise TypeError("Cannot subtract a non-matrix object from matrix.")
    
    def __mul__(self, obj):
        if type(obj) == int or type(obj) == float:
            return Matrix2X2(
                self.elemA * obj,
                self.elemB * obj,
                self.elemC * obj,
                self.elemD * obj
            )
        elif type(obj) == Matrix2X2:
            return Matrix2X2(
                self.elemA * obj.elemA + self.elemB * obj.elemC,
                self.elemA * obj.elemB + self.elemB * obj.elemD,
                self.elemC * obj.elemA + self.elemD * obj.elemC,
                self.elemC * obj.elemB + self.elemD * obj.elemD
            )
        elif type(obj) == Vector2D:
            return Vector2D(
                run = self.elemA * obj.x + self.elemB * obj.y,
                rise = self.elemC * obj.x + self.elemD * obj.y
            )
        else:
            raise TypeError("Cannot multiply matrix with  non-int, non-float, non-matrix or non-vector object.")

class Rotation(Matrix2X2):
    
    def __init__(self, rotationInRadians:EulerAngle, relativeTo:Point2D = None):
        if relativeTo == None:
            self.__rotationSize = rotationInRadians.radians
            super().__init__(
                math.cos(self.__rotationSize),
                math.sin(self.__rotationSize),
                math.sin(self.__rotationSize),
                math.cos(self.__rotationSize)
            )
    
class Scaling(Matrix2X2):

    def __init__(self, center, scaleFactor) -> None:
        super().__init__(0, 0, 0, 0)