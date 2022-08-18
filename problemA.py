from Package1 import MathObjects as Math
import math

VectA = Math.Vector2D(rise = 4, run = 3)

clock180 = Math.EulerAngle(math.pi)

MatR = Math.Rotation(clock180)


print(MatR.elemA, MatR.elemB, MatR.elemC, MatR.elemD)

VectR = MatR * VectA

print(VectA)
print(VectR)