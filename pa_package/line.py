from .point import Point


class Line:
    def __init__(self, p1, p2):
        if p1.x == p2.x and p1.y == p2.y:
            raise ValueError("A line requires two different points.")

        self.p1 = p1
        self.p2 = p2

    def length(self):
        return self.p1.distance_to(self.p2)

    def perpendicular_from_point(self, point):
        """
        Returns a Line from the given point to the closest point on this line.
        """

        x1, y1 = self.p1.x, self.p1.y
        x2, y2 = self.p2.x, self.p2.y
        x3, y3 = point.x, point.y

        dx = x2 - x1
        dy = y2 - y1

        t = ((x3 - x1) * dx + (y3 - y1) * dy) / (dx ** 2 + dy ** 2)

        foot_x = x1 + t * dx
        foot_y = y1 + t * dy

        foot = Point(foot_x, foot_y)

        return Line(point, foot)

    def distance_from_point(self, point):
        perpendicular = self.perpendicular_from_point(point)
        return perpendicular.length()

    def __str__(self):
        return f"Line({self.p1}, {self.p2})"