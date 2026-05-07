import unittest

from pa_package.point import Point
from pa_package.line import Line


class TestPoint(unittest.TestCase):

    def test_distance_between_two_points(self):
        p1 = Point(0, 0)
        p2 = Point(3, 4)

        self.assertEqual(p1.distance_to(p2), 5)


class TestLine(unittest.TestCase):

    def test_line_length(self):
        p1 = Point(0, 0)
        p2 = Point(3, 4)

        line = Line(p1, p2)

        self.assertEqual(line.length(), 5)

    def test_vertical_line_distance_from_point(self):
        line = Line(Point(2, 0), Point(2, 5))
        point = Point(5, 3)

        self.assertEqual(line.distance_from_point(point), 3)

    def test_horizontal_line_distance_from_point(self):
        line = Line(Point(0, 4), Point(5, 4))
        point = Point(3, 1)

        self.assertEqual(line.distance_from_point(point), 3)

    def test_perpendicular_from_point_to_line(self):
        line = Line(Point(0, 0), Point(4, 0))
        point = Point(2, 3)

        perpendicular = line.perpendicular_from_point(point)

        self.assertEqual(perpendicular.p1.x, 2)
        self.assertEqual(perpendicular.p1.y, 3)
        self.assertEqual(perpendicular.p2.x, 2)
        self.assertEqual(perpendicular.p2.y, 0)
        self.assertEqual(perpendicular.length(), 3)

    def test_cannot_create_line_from_same_point(self):
        with self.assertRaises(ValueError):
            Line(Point(1, 1), Point(1, 1))


if __name__ == "__main__":
    unittest.main()