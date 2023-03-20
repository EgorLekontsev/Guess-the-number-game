import tkinter as tk
from tkinter.messagebox import showerror
import random

class GuessNumberGame:
    def __init__(self, master):
        self.master = master
        master.title("Угадай число")

        self.label = tk.Label(master, text="Угадай число от 1 до 100")
        self.label.pack()

        self.guess_button = tk.Button(master, text="Угадать число", command=self.guess_number)
        self.guess_button.pack()

        self.new_game_button = tk.Button(master, text="Новая игра", command=self.new_game)
        self.new_game_button.pack()

        self.input = tk.Entry(master)
        self.input.pack()

        self.number = random.randint(1, 100)
        self.guesses = 0

    def guess_number(self):
        try:
            guess = int(self.input.get())
        except:
            showerror("Ошибка","Впишите число!")
        self.guesses += 1

        if guess == self.number:
            message = f"Поздравляем! Загаданное число было {self.number}. Вы угадали его за {self.guesses} попыток."
            self.label.config(text=message)
        elif guess < self.number:
            self.label.config(text="Загаданное число больше.")
        elif guess > self.number:
            self.label.config(text="Загаданное число меньше.")


    def new_game(self):
        self.number = random.randint(1, 100)
        self.guesses = 0
        self.label.config(text="Угадай число от 1 до 100")

root = tk.Tk()
root.resizable(0, 0)
game = GuessNumberGame(root)
root.mainloop()
