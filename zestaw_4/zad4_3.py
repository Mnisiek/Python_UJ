"""
Napisać iteracyjną wersję funkcji factorial(n) obliczającej silnię. """


def factorial(n: int) -> int:
    result = 1
    for i in range(2, n+1):
        result *= i

    return result


for i in range(0, 8):
    print(factorial(i))
