"""
Co jest złego w kodzie: """


L = [3, 5, 4] ; L = L.sort()
# Drugie wyrażenie sortuje listę, ale jako wynik zwraca wartość None,
# która jest następnie przypisywana do L. Powinno być: L.sort()

x, y = 1, 2, 3
# Liczba zmiennych po lewej stronie nie zgadza się z liczbą
# wartości do przypisania (2 a 3)

X = 1, 2, 3 ; X[1] = 4
# Pierwsze wyrażenie tworzy krotkę, która jest niemodyfikowalnym typem
# danych. W związku z tym nie można zmieniać wartości krotki.

X = [1, 2, 3] ; X[3] = 4
# Drugie wyrażenie odwołuje do elementu będącego poza zakresem
# (czwarty element)

X = "abc" ; X.append("d")
# Napisy są niemodyfikowalne

L = list(map(pow, range(8)))
# Nie podano wymaganych argumentów dla wywołania funkcji pow
