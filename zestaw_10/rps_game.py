"""
Napisać program z GUI, który realizuje grę Papier-Kamień-Nożyce użytkownika
z komputerem. Wybór komputera jest losowany. Program może zawierać trzy
przyciski dla każdego wyboru użytkownika (P, K, N) oraz etykietę wyświetlającą
wybór człowieka, komputera i wynik gry. """


import tkinter as tk
from random import randint

# zmienne globalne
human_guess = -1
computer_guess = -1
result_txt = ""


# funkcja odpowiedzialna za losowanie wyboru komputera oraz
# zwracająca wynik rozgrywki
def play_rps(choice):
    global human_guess, computer_guess, result_txt

    # (wybór_człowieka, wybór komputera): wynik [dla człowieka]
    # 0 - papier, 1 - kamień, 2 - nożyce
    human_computer_win = {
        (0, 1): "Wygrywasz!",
        (0, 2): "Przegrywasz!",
        (1, 0): "Przegrywasz!",
        (1, 2): "Wygrywasz!",
        (2, 0): "Wygrywasz!",
        (2, 1): "Przegrywasz!",
    }

    human_guess = choice
    computer_guess = randint(0, 2)

    if human_guess == computer_guess:
        result_txt = "Remis"
    else:
        result_txt = human_computer_win.get((human_guess, computer_guess), "")

    human_choice_text = ["Papier 📃", "Kamień 🪨", "Nożyce ✂️"][human_guess]
    computer_choice_text = ["Papier 📃", "Kamień 🪨", "Nożyce ✂️"][computer_guess]

    label_human_choice.config(text=f"Człowiek: {human_choice_text}")
    label_computer_choice.config(text=f"Komputer: {computer_choice_text}")
    label_result.config(text=f"Wynik: {result_txt}")


# konfiguracja wyświetlanego okna
root = tk.Tk()
root.title("Papier, Kamień, Nożyce")
root.geometry("600x400")

label = tk.Label(root, text="Wybierz jedną z trzech możliwości...", 
                 font=("Arial", 18), height=3, fg="blue")
label.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

button_paper = tk.Button(button_frame, text="Papier 📃", width=15, height=2,
                          font=("Arial", 14), command=lambda: play_rps(0))
button_rock = tk.Button(button_frame, text="Kamień 🪨", width=15, height=2,
                          font=("Arial", 14), command=lambda: play_rps(1))
button_scissors = tk.Button(button_frame, text="Nożyce ✂️", width=15, height=2,
                          font=("Arial", 14), command=lambda: play_rps(2))

button_paper.pack(side="left", padx=5, pady=5)
button_rock.pack(side="left", padx=5, pady=5)
button_scissors.pack(side="left", padx=5, pady=5)


label_human_choice = tk.Label(root, text="Człowiek: ", font=("Arial", 14))
label_computer_choice = tk.Label(root, text="Komputer: ", font=("Arial", 14))
label_result = tk.Label(root, text="Wynik: ", font=("Arial", 14), fg="blue")

label_human_choice.pack(pady=5)
label_computer_choice.pack(pady=5)
label_result.pack(pady=5)

root.mainloop()
