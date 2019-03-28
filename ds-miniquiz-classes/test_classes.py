import unittest
import math
from classes import Point, Triangle


class TestPoint(unittest.TestCase):

    def test_distance(self):
        p1 = Point(-1, -1)
        p2 = Point(2, 3)
        p3 = Point(0, -2)
        self.assertAlmostEqual(p1.distance(p3), math.sqrt(2))
        self.assertAlmostEqual(p1.distance(p2), 5.0)

    def test_perimeter(self):
        p1 = Point(-1, -1)
        p2 = Point(2, 3)
        p4 = Point(-1, 3)
        self.assertAlmostEqual(Triangle(p1, p2, p4).perimeter(), 12)

    def test_is_line(self):
        p1 = Point(-1, -1)
        p2 = Point(2, 3)
        p4 = Point(-1, 3)
        p5 = Point(-4, -5)
        self.assertFalse(Triangle(p1, p2, p4).is_line())
        self.assertTrue(Triangle(p1, p2, p5).is_line())


if __name__ == '__main__':
    unittest.main()
