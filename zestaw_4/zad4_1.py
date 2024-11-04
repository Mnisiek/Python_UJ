"""
Jaki będzie wynik poniższego kodu i dlaczego? """


X = "qwerty"

def func():
    print(X)

func()
# po wywołaniu funkcji func() zostanie wyświetlony napis "qwerty",
# ponieważ zmienna X jest globalna i dostępna dla całego kodu znajdującego
# się po jej definicji (więc też dla funkcji func())

###############################################################################
X = "qwerty"

def func():
    X = "abc"  # noqa: F841

func()
print(X)
# zostanie wyświetlone "qwerty", ponieważ zmienna X zdefiniowana
# w ciele funkcji jest zmienną lokalną, która po wyjściu z funkcji
# jest niszczona (funkcja print() widzi tylko zmienną globalną X)

###############################################################################
X = "qwerty"

def func():
    global X
    X = "abc"

func()
print(X)
# wyświetlony zostanie napis "abc"; funkcja deklaruje zmienną X
# w swoim ciele jako globalną i dlatego przypisanie X = "abc"
# modyfikuje wartość zmiennej globalnie w całym programie
