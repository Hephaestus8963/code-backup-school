from Package1.Classes import Point2D, Vector2D

Origin = Point2D.origin()
PointP = Point2D(3, 4)

PosP = Vector2D(Origin, PointP)

VectorAB = Vector2D(run = 6, rise = 8)

print(PosP)
print(VectorAB)
print(PosP.areParallel(VectorAB))
