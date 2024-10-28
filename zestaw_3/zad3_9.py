"""
Mamy daną listę sekwencji (listy lub krotki) różnej długości
zawierających liczby. Znaleźć listę zawierającą sumy liczb z tych sekwencji.
Przykładowa sekwencja [[],[4],(1,2),[3,4],(5,6,7)],
spodziewany wynik [0,4,3,7,18]. """


seq = [[], [4], (1, 2), [3, 4], (5, 6, 7)]
# List comprehension
result = [sum(element) for element in seq]


print(result)
