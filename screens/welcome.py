import tkinter as tk
from tkinter import ttk
from messages import MESSAGES


class Welcome(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent, bg="white")
        self.app = app

        tk.Label(
            self, text=MESSAGES.welcome_title,
            bg="white", font=("Arial", 22)
        ).pack(pady=60)

        ttk.Button(
            self, text=MESSAGES.start_button, width=15,
            command=lambda: app.show("NameInput")
        ).pack()
