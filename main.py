from pa_package.point import Point
from pa_package.line import Line

p1 = Point(0, 0)
p2 = Point(3, 4)

line = Line(p1, p2)

print(line)
print("Length:", line.length())
