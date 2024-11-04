"""
Napisać funkcję odwracanie(L, left, right) odwracającą kolejność elementów
na liście od numeru left do right włącznie. Lista jest modyfikowana w miejscu
(in place). Rozważyć wersję iteracyjną i rekurencyjną. """


def odwracanie(L: list, left: int, right: int) -> None:
    while left < right:
        L[left], L[right] = L[right], L[left]
        left += 1
        right -= 1


def odwracanie_rek(L: list, left: int, right: int) -> None:
    if left >= right:
        return
    L[left], L[right] = L[right], L[left]
    odwracanie_rek(L, left+1, right-1)


L = [num for num in range(1, 16)]
odwracanie(L, 4, 6)
print(L)

odwracanie_rek(L, 9, 12)
print(L)
