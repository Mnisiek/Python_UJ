"""
Napisać program pobierający w pętli od użytkownika liczbę rzeczywistą x
(typ float) i wypisujący x oraz trzecią potęgę x. Zatrzymanie programu
następuje po wpisaniu z klawiatury stop. Jeżeli użytkownik wpisze napis
zamiast liczby, to program ma wypisać komunikat o błędzie i kontynuować pracę. """


while True:
    x = input("Podaj liczbę: ")
    if (x == "stop"):
        print("Koniec")
        break
    elif x.isalpha():
        print("Błąd")
    else:
        x = float(x)
        print(x, pow(x, 3))
