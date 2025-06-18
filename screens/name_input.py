import tkinter as tk
from tkinter import ttk
from messages import MESSAGES


class NameInput(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent, bg="white")
        self.app = app

        # Заголовок
        tk.Label(
            self, text=MESSAGES.name_title,
            bg="white", font=("Arial", 18)
        ).pack(pady=40)

        # Поле ввода
        self.name_var = tk.StringVar()
        entry = ttk.Entry(
            self, textvariable=self.name_var,
            width=28, font=("Arial", 14)
        )
        entry.pack()
        entry.insert(0, MESSAGES.name_placeholder)

        # Кнопки
        btn_row = tk.Frame(self, bg="white")
        btn_row.pack(pady=30)

        ttk.Button(
            btn_row, text=MESSAGES.back_main, width=15,
            command=lambda: app.show("Welcome")
        ).grid(row=0, column=0, padx=15)

        ttk.Button(
            btn_row, text=MESSAGES.name_next, width=15,
            command=lambda: app.show("SelectMed")
        ).grid(row=0, column=1, padx=15)
