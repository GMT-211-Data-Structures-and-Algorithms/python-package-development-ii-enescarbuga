from .point import Point

class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def length(self):
        return ((self.p1.x - self.p2.x)**2 + (self.p1.y - self.p2.y)**2) ** 0.5

    def __str__(self):
        return f"Line({self.p1}, {self.p2})"
