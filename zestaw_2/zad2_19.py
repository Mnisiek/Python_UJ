"""
Na liście L mamy liczby jedno-, dwu- i trzycyfrowe dodatnie. Chcemy zbudować
napis z trzycyfrowych bloków, gdzie liczby jedno- i dwucyfrowe będą miały
blok dopełniony zerami, np. 007, 024. Wskazówka: str.zfill(). """


L = [32, 1, 958, 46, 6, 8, 324, 45, 453, 2, 67, 4, 321]
result = ''.join(str(num).zfill(3) for num in L)
print(result)
