"""
Zbudować napis stworzony z pierwszych znaków wyrazów z wiersza line.
Zbudować napis stworzony z ostatnich znaków wyrazów z wiersza line. """


line = 'Napis \nwielo-\nwierszowy, napis    napis.'
word_list = line.split()

first_letters_word = ''
for i in range(len(word_list)):
    first_letters_word += word_list[i][0]
print(first_letters_word)


last_letters_word = ''
for i in range(len(word_list)):
    last_letters_word += word_list[i][-1]
print(last_letters_word)


# inny sposób, z wykorzystaniem .join
# first_letters_word = ''.join(word[0] for word in word_list)
# print(first_letters_word)

# last_letters_word = ''.join(word[-1] for word in word_list)
# print(last_letters_word)
