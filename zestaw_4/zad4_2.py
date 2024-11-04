"""
Rozwiązania zadań 3.5 i 3.6 z poprzedniego zestawu zapisać w postaci funkcji,
które zwracają pełny string przez return. Funkcje nie powinny pytać użytkownika
o dane, tylko korzystać z argumentów.

def make_ruler(n): pass

def make_grid(rows, cols): pass
"""


def make_ruler(n: int) -> str:
    result = "|"

    for i in range(n):
        result += "....|"
    result += '\n0'

    for j in range(1, n+1):
        spacing = 5 - len(str(j))
        result += " " * spacing + str(j)
    return result


def make_grid(rows: int, cols: int) -> str:
    line1 = "+---" * cols + "+\n" 
    line2 = "|   " * cols + "|\n"
    
    result = ""
    for i in range(rows):
        result += line1 + line2
    result += line1
    return result


print(make_ruler(14))
print()
print(make_grid(4, 7))
