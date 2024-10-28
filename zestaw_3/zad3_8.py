"""
Dla dwóch sekwencji liczb lub znaków znaleźć: (a) listę elementów
występujących jednocześnie w obu sekwencjach (bez powtórzeń),
(b) listę wszystkich elementów z obu sekwencji (bez powtórzeń). """


seq1 = [2, 5, 21, 7, 8, 12, 235, 2, 14, 767, 23, 432]
seq2 = [7, 98, 432, 24, 14, 6, 2, 36, 32, 46, 756]

# a)
product = list(set(seq1).intersection(set(seq2)))
print(product)

# b)
summa = list(set(seq1).union(set(seq2)))
print(summa)
