"""
Napisać program rysujący "miarkę" o zadanej długości.
Należy prawidłowo obsłużyć liczby składające się z kilku
cyfr (ostatnia cyfra liczby ma znajdować się pod znakiem kreski pionowej).
Należy zbudować pełny string, a potem go wypisać.

|....|....|....|....|....|....|....|....|....|....|....|....|
0    1    2    3    4    5    6    7    8    9   10   11   12
"""


def tape_measure(length: int) -> None:
    tape_upper = "|"
    tape_bottom = "0"

    for i in range(length):
        tape_upper += "....|"

    for j in range(1, length + 1):
        spacing = 5 - len(str(j))
        tape_bottom += " " * spacing + str(j)

    print(tape_upper)
    print(tape_bottom)


tape_measure(15)
tape_measure(4)
