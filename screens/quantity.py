import tkinter as tk
from tkinter import ttk
from config import PILLS
from messages import MESSAGES


class Quantity(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent)
        self.app = app
        self.qty = tk.IntVar(value=1)

        self.label = ttk.Label(self, font=("Arial", 18))
        self.label.pack(pady=10)

        box = ttk.Frame(self)
        box.pack(pady=10)
        ttk.Button(box, text=MESSAGES.minus_button, width=5,
                   command=lambda: self._inc(-1)).grid(row=0, column=0)
        ttk.Label(box, textvariable=self.qty, width=5, anchor="center",
                  font=("Arial", 16)).grid(row=0, column=1)
        ttk.Button(box, text=MESSAGES.plus_button, width=5,
                   command=lambda: self._inc(+1)).grid(row=0, column=2)

        ttk.Button(self, text=MESSAGES.ok_button, command=self._confirm)\
            .pack(pady=20, ipadx=30, ipady=5)

    def tkraise(self, *args, **kwargs):
        super().tkraise(*args, **kwargs)
        pill_code = self.app.current_pill
        self.label.config(text=f"How many {PILLS[pill_code]['name']}?")
        self.qty.set(1)

    def _inc(self, delta):
        val = max(1, self.qty.get() + delta)
        self.qty.set(val)

    def _confirm(self):
        self.app.add_item(self.app.current_pill, self.qty.get())
        self.app.show("AddMore")
