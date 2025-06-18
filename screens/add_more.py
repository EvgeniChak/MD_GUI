import tkinter as tk
from tkinter import ttk
from messages import MESSAGES

class AddMore(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent)
        self.app = app
        ttk.Label(self, text=MESSAGES.add_more_title, font=("Arial", 18))\
            .pack(pady=40)

        btns = ttk.Frame(self)
        btns.pack()
        ttk.Button(btns, text=MESSAGES.add_more_yes, width=12,
                   command=lambda: app.show("SelectMed")).grid(row=0, column=0, padx=20)
        ttk.Button(btns, text=MESSAGES.add_more_no, width=12,
                   command=lambda: app.show("Summary")).grid(row=0, column=1, padx=20)
