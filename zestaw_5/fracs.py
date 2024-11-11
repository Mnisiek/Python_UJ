"""
Stworzyć plik fracs.py i zapisać w nim funkcje do działań na ułamkach.
Ułamek będzie reprezentowany przez listę dwóch liczb całkowitych
[licznik, mianownik]. Napisać kod testujący moduł fracs. Nie należy
korzystać z klasy Fraction z modułu fractions. Można wykorzystać funkcję
fractions.gcd() implementującą algorytm Euklidesa. """


# Changed in version 3.9: The math.gcd() function is now used to
# normalize the numerator and denominator. [docs.python.org]
from math import gcd
import unittest


def reduce_frac(frac):
    divisor = gcd(frac[0], frac[1])
    frac[0] //= divisor
    frac[1] //= divisor
    if not is_positive(frac) and frac[1] < 0:
        frac[0], frac[1] = -frac[0], -frac[1] 
    return frac

def add_frac(frac1, frac2):
    result = [None] * 2
    result[0] = frac1[0]*frac2[1] + frac2[0]*frac1[1]
    result[1] = frac1[1]*frac2[1]
    return reduce_frac(result)

def sub_frac(frac1, frac2):
    result = [None] * 2
    result[0] = frac1[0]*frac2[1] - frac2[0]*frac1[1]
    result[1] = frac1[1]*frac2[1]
    return reduce_frac(result)


def mul_frac(frac1, frac2):
    result = [None] * 2
    result[0] = frac1[0]*frac2[0]
    result[1] = frac1[1]*frac2[1]
    return reduce_frac(result)

def div_frac(frac1, frac2):
    result = [None] * 2
    result[0] = frac1[0]*frac2[1]
    result[1] = frac1[1]*frac2[0]
    return reduce_frac(result)

def is_positive(frac):
    if frac[0] > 0 and frac[1] > 0:
        return True
    elif frac[0] < 0 and frac[1] < 0:
        return True
    else:
        return False

def is_zero(frac):
    return True if frac[0] == 0 else False

def cmp_frac(frac1, frac2):
    if frac1[0] == frac2[0] and frac2[1] == frac2[1] or \
    is_zero(frac1) and is_zero(frac2):
        return 0
    elif is_positive(sub_frac(frac1, frac2)):
        return -1
    else:
        return 1

def frac2float(frac):
    return frac[0] / frac[1]


class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]

    def test_add_frac(self):
        self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])

    def test_sub_frac(self):
        self.assertEqual(sub_frac([6, 8], [1, 5]), [11, 20])

    def test_mul_frac(self):
        self.assertEqual(mul_frac([7, 5], [1, 3]), [7, 15])

    def test_div_frac(self):
        self.assertEqual(div_frac([7, -3], [2, 5]), [-35, 6])

    def test_is_positive_false(self):
        self.assertEqual(is_positive([-4, 9]), False)

    def test_is_positive_true(self):
        self.assertEqual(is_positive([-4, -9]), True)

    def test_is_zero_true(self):
        self.assertEqual(is_zero([0, 2]), True)

    def test_is_zero_false(self):
        self.assertEqual(is_zero([1, 2]), False)

    def test_cmp_frac1(self):
        self.assertEqual(cmp_frac([8, 9], [1, 3]), -1)

    def test_cmp_frac2(self):
        self.assertEqual(cmp_frac([1, 4], [4, 5]), 1)

    def test_cmp_frac3(self):
        self.assertEqual(cmp_frac([1, 3], [1, 3]), 0)

    def test_frac2float(self):
        self.assertAlmostEqual(frac2float([2, 5]), 0.4, places=7)

    def tearDown(self):
        self.zero = None

if __name__ == '__main__':
    unittest.main()
