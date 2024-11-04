"""
Napisać iteracyjną wersję funkcji fibonacci(n) obliczającej
n-ty wyraz ciągu Fibonacciego. """


def fibonacci(n: int) -> int:
    a, b, c = 1, 1, 1

    for _ in range(1, n):
        c = a + b
        a, b = b, c
    
    return c


for i in range(10):
    print(fibonacci(i))
