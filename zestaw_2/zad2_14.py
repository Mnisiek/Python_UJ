"""
Znaleźć: (a) najdłuższy wyraz, (b) długość najdłuższego wyrazu w napisie line. """


line = 'Napis \nwielo-\nwierszowy, napis    napis.'
word_list = line.split()
longest_word = max(word_list, key=len)
print(longest_word)
print(len(longest_word))
