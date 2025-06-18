import tkinter as tk
from tkinter import ttk
from messages import MESSAGES

GOODBYE_MS = 3_000  # 3 с

class Goodbye(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent, bg="white")
        self.app = app

        ttk.Label(self, text=MESSAGES.goodbye_title, background="white",
                  font=("Arial", 20)).pack(pady=60)

        ttk.Button(self, text=MESSAGES.back_main, width=18,
                   command=lambda: app.show("Welcome")).pack()

        # авто-возврат
        self.after(GOODBYE_MS, lambda: app.show("Welcome"))
