"""
Napisać program rysujący prostokąt zbudowany z małych kratek.
Należy zbudować pełny string, a potem go wypisać.
Przykładowy prostokąt składający się 2x4 pól ma postać:

+---+---+---+---+
|   |   |   |   |
+---+---+---+---+
|   |   |   |   | 
+---+---+---+---+
"""


def draw_rectangle(rows: int, cols: int) -> None:
    line1 = "+{:-^4}".format("---") * cols + "+"
    line2 = "|{:<4}".format(" ") * cols + "|"
    
    rect = ""
    for i in range(rows):
        rect += line1 + "\n" + line2 + "\n"
    rect += line1
    
    print(rect)


draw_rectangle(3, 8)
print()
draw_rectangle(1, 1)
