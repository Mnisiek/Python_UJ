"""
Posortować wyrazy z napisu line raz alfabetycznie, a raz pod
względem długości. Wskazówka: funkcja wbudowana sorted(). """


line = 'Napis \nwielo-\nwierszowy, dalsza część...'
word_list = line.split()
alphabetical_order = sorted(word.lower() for word in word_list)
print(alphabetical_order)

length_order = sorted(word_list, key=len)
print(length_order)