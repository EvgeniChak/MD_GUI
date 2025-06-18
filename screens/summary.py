import tkinter as tk
from tkinter import ttk
from config import PILLS
from messages import MESSAGES

class Summary(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent)
        self.app = app

        ttk.Label(self, text=MESSAGES.summary_title, font=("Arial", 18)).pack(pady=10)
        self.box = ttk.Frame(self)
        self.box.pack()

        btns = ttk.Frame(self)
        btns.pack(pady=10)
        ttk.Button(btns, text=MESSAGES.send_btn, width=12,
                   command=self._send).grid(row=0, column=0, padx=15)
        ttk.Button(btns, text=MESSAGES.cancel_btn, width=12,
                   command=self._cancel).grid(row=0, column=1, padx=15)

    def tkraise(self, *args, **kwargs):
        super().tkraise(*args, **kwargs)
        for w in self.box.winfo_children():
            w.destroy()

        for i, (code, qty) in enumerate(self.app.order.items(), 1):
            ttk.Label(self.box, text=f"{i}. {PILLS[code]['name']}",
                      width=20, anchor="w").grid(row=i, column=0, sticky="w")
            ttk.Label(self.box, text=f"×{qty}", width=5)\
                .grid(row=i, column=1, sticky="e")

        cmd = (self.app.build_json() if self.app.json_mode.get()
               else self.app.build_serial())
        ttk.Label(self, text=cmd, foreground="blue").pack(pady=5)

    def _send(self):
        self.app.send_order()
        self.app.show("Goodbye")

    def _cancel(self):
        self.app.clear_order()
        self.app.show("Welcome")
