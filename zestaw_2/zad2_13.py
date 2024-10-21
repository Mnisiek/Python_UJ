"""
Znaleźć łączną długość wyrazów w napisie line.
Wskazówka: można skorzystać z funkcji sum(). """


line = 'Napis \nwielo-\nwierszowy, napis    napis.'
word_list = line.split()
overall_length = sum(len(word) for word in word_list)
print(overall_length)
