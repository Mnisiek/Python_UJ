"""
W pliku fracs.py zdefiniować klasę Frac wraz z potrzebnymi metodami.
Ułamek jest reprezentowany przez parę liczb całkowitych.
Napisać kod testujący moduł fracs. """


from math import gcd   # Py3
import unittest


class Frac:
    """Klasa reprezentująca ułamek."""

    def __init__(self, x=0, y=1):
        if y == 0:
            raise ValueError("Mianownik nie może być równy zero.")
        divisor = gcd(x, y)
        self.x = x // divisor
        self.y = y // divisor
        if self.y < 0:  # pozbywamy się minusa z mianownika ułamka
            self.x, self.y = -self.x, -self.y

    def __str__(self):         # zwraca "x/y" lub "x" dla y=1
        return f"{self.x}" if self.y == 1 else f"{self.x}/{self.y}"
    
    def __repr__(self):        # zwraca "Frac(x, y)"
        return f"Frac({self.x}, {self.y})"

    def __eq__(self, other):    # Py2.7 i Py3
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        return self.x * other.y < self.y * other.x

    def __le__(self, other):
        return self.x * other.y <= self.y * other.x

    def __add__(self, other):  # frac1 + frac2
        return Frac(self.x * other.y + other.x * self.y, self.y * other.y)

    def __sub__(self, other):  # frac1 - frac2
        return Frac(self.x * other.y - other.x * self.y, self.y * other.y)

    def __mul__(self, other):  # frac1 * frac2
        return Frac(self.x * other.x, self.y * other.y)

    def __truediv__(self, other):  # frac1 / frac2, Py3
        return Frac(self.x * other.y, self.y * other.x)

    # def __floordiv__(self, other):  # frac1 // frac2, opcjonalnie

    # def __mod__(self, other):  # frac1 % frac2, opcjonalnie

    # operatory jednoargumentowe
    def __pos__(self):  # +frac = (+1)*frac
        return self

    def __neg__(self):  # -frac = (-1)*frac
        return Frac(-self.x, self.y)

    def __invert__(self):  # odwrotnosc: ~frac
        return Frac(self.y, self.x)

    def __float__(self):       # float(frac)
        return self.x / self.y

    def __hash__(self):
        return hash(float(self))   # immutable fracs
        # w Pythonie set([2]) == set([2.0])
        # chcemy set([2]) == set([Frac(2)])


# Kod testujący moduł.

class TestFrac(unittest.TestCase):
    def test_str(self):
        self.assertEqual(str(Frac(5, 7)), "5/7")
        self.assertEqual(str(Frac(6, 1)), "6")

    def test_repr(self):
        self.assertEqual(repr(Frac(3, 2)), "Frac(3, 2)")

    def test_eq(self):
        self.assertTrue(Frac(1, 2) == Frac(2, 4))
        self.assertFalse(Frac(1, 2) == Frac(3, 4))

    def test_comp(self):
        self.assertTrue(Frac(1, 2) < Frac(3, 4))
        self.assertTrue(Frac(1, 2) <= Frac(2, 4))
        self.assertFalse(Frac(3, 4) < Frac(1, 2))

    def test_add(self):
        self.assertEqual(Frac(1, 2) + Frac(1, 3), Frac(5, 6))

    def test_sub(self):
        self.assertEqual(Frac(6, 8) - Frac(1, 5), Frac(11, 20))

    def test_mul(self):
        self.assertEqual(Frac(7, 5) * Frac(1, 3), Frac(7, 15))

    def test_truediv(self):
        self.assertEqual(Frac(7, -3) / Frac(2, 5), Frac(-35, 6))

    def test_pos(self):
        self.assertEqual(+Frac(1, 3), Frac(1, 3))
        self.assertEqual(+Frac(1, 3), Frac(-1, -3))

    def test_neg(self):
        self.assertEqual(-Frac(1, 2), Frac(-1, 2))
        self.assertEqual(-Frac(1, 2), Frac(1, -2))

    def test_invert(self):
        self.assertEqual(~Frac(3, 4), Frac(4, 3))

    def test_float(self):
        self.assertAlmostEqual(float(Frac(2, 5)), 0.4, places=7)

    def test_hash(self):
        self.assertEqual(hash(Frac(1, 2)), hash(Frac(2, 4)))

if __name__ == "__main__":
    unittest.main()
    