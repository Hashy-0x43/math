import math

circledegree = 360

radius = float(input("Radius = "))
circumference = (radius * 2) * math.pi

angle = float(input("Angle = "))

arclength = (angle / circledegree) * circumference

print(arclength)
