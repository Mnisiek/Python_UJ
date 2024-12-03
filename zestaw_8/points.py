"""
W pliku points.py zdefiniować klasę Point wraz z potrzebnymi metodami.
Punkty są traktowane jak wektory zaczepione w początku układu współrzędnych,
o końcu w położeniu (x, y). Napisać kod testujący moduł points."""

from math import sqrt
import unittest


class Point:
    """Klasa reprezentująca punkty na płaszczyźnie."""

    def __init__(self, x, y):  # konstuktor
        self.x = x
        self.y = y

    def __str__(self):        # zwraca string "(x, y)"
        return "({}, {})".format(self.x, self.y)

    def __repr__(self):        # zwraca string "Point(x, y)"
        return "Point({}, {})".format(self.x, self.y)

    def __eq__(self, other):   # obsługa point1 == point2
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):        # obsługa point1 != point2
        return not self == other

    # Punkty jako wektory 2D.
    def __add__(self, other):  # v1 + v2
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):  # v1 - v2
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):  # v1 * v2, iloczyn skalarny, zwraca liczbę
        return self.x * other.x + self.y * other.y

    def cross(self, other):         # v1 x v2, iloczyn wektorowy 2D, zwraca liczbę
        return self.x * other.y - self.y * other.x

    def length(self):         # długość wektora
        return sqrt(self.x * self.x + self.y * self.y)

    def __hash__(self):
        return hash((self.x, self.y))   # bazujemy na tuple, immutable points



# Kod testujący moduł.

class TestPoint(unittest.TestCase):
    def test_str(self):
        self.assertEqual(str(Point(4, 7)), "(4, 7)")

    def test_repr(self):
        self.assertEqual(repr(Point(2, 9)), "Point(2, 9)")

    def test_eq(self):
        self.assertTrue(Point(1, 3) == Point(1, 3))
        self.assertFalse(Point(2, 5) == Point(2, 4))

    def test_ne(self):
        self.assertTrue(Point(1, 2) != Point(2, 3))
        self.assertFalse(Point(1, 2) != Point(1, 2))

    def test_add(self):
        self.assertEqual(Point(1, 2) + Point(3, 4), Point(4, 6))

    def test_sub(self):
        self.assertEqual(Point(5, 6) - Point(3, 4), Point(2, 2))

    def test_mul(self):
        self.assertEqual(Point(1, 2) * Point(3, 4), 11)

    def test_cross(self):
        self.assertEqual(Point(1, 2).cross(Point(3, 4)), -2)

    def test_length(self):
        self.assertAlmostEqual(Point(3, 4).length(), 5)

    def test_hash(self):
        self.assertEqual(hash(Point(1, 2)), hash(Point(1, 2)))
        self.assertNotEqual(hash(Point(1, 2)), hash(Point(1, 3)))

if __name__ == "__main__":
    unittest.main()
