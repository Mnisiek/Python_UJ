"""
Na liście L znajdują się liczby całkowite dodatnie. Stworzyć napis będący
ciągiem cyfr kolejnych liczb z listy L. """


L = [3, 7, 2, 5, 10, 14, 8]
numbers_string = ''.join(str(element) for element in L)
print(numbers_string)