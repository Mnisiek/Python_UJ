"""
Czy podany kod jest poprawny składniowo w Pythonie? Jeśli nie, to dlaczego? """


x = 2; y = 3;
if (x > y):
    result = x;
else:
    result = y;
# Kod jest poprawny składniowo, przypisuje do zmiennej result większą z liczb


# for i in "axby": if ord(i) < 100: print (i)
# Kod nie jest poprawny składniowo. Żeby działał prawidłowo, blok if powinien
# być wcięty:
for i in "axby":
    if ord(i) < 100: print (i)


for i in "axby": print (ord(i) if ord(i) < 100 else i)
# Kod jest zapisany poprawnie
