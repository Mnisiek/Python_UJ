"""
Mamy dany napis wielowierszowy line. Podać sposób obliczenia liczby wyrazów
w napisie. Przez wyraz rozumiemy ciąg "czarnych" znaków, oddzielony od innych
wyrazów białymi znakami (spacja, tabulacja, newline). """


line = 'Napis \nwielo-\nwierszowy, napis    napis.'
word_list = line.split()
print(line)
print(len(word_list)) # wyświetla liczbę elementów listy przechowującej wyrazy
