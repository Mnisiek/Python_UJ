"""
Wypisać w pętli liczby od 0 do 30 z wyjątkiem liczb podzielnych przez 3. """


for num in range(30):
    if num % 3 != 0:
        print(num)
