"""
Stworzyć następujące iteratory nieskończone:
(a) zwracający 0, 1, 0, 1, 0, 1, ...,
(b) zwracający przypadkowo jedną wartość z ("N", "E", "S", "W")
[błądzenie przypadkowe na sieci kwadratowej 2D],
(c) zwracający 0, 1, 2, 3, 4, 5, 6, 0, 1, 2, 3, 4, 5, 6, ... 
[numery dni tygodnia]. """

import itertools
import random

# (a)
iter1 = itertools.cycle(range(0, 2))
for elem in iter1:
    print(elem)


# (b)
iter2 = (random.choice(("N", "E", "S", "W")) for _ in iter(int, 1))
for elem in iter2:
    print(elem)


# (c)
iter3 = itertools.cycle(range(0, 7))
for elem in iter3:
    print(elem)
