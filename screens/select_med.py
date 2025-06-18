import tkinter as tk
from tkinter import ttk
from config import PILLS
from messages import MESSAGES

class SelectMed(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent, bg="white")
        self.app = app

        tk.Label(
            self, text=MESSAGES.select_med_title,
            bg="white", font=("Arial", 18)
        ).pack(pady=10)

        grid = ttk.Frame(self, padding=10)
        grid.pack()

        sorted_items = sorted(PILLS.items(), key=lambda kv: kv[1]["name"])
        for idx, (code, meta) in enumerate(sorted_items):
            row, col = divmod(idx, 4)          # 4×4 как в презентации
            btn = ttk.Button(
                grid, width=20,
                text=meta["name"],
                command=lambda c=code: self._choose(c)
            )
            btn.grid(row=row, column=col, padx=6, pady=6)

        bottom = tk.Frame(self, bg="white")  # ← tk.Frame
        bottom.pack(fill="x", pady=10)

        ttk.Checkbutton(
            bottom, text=MESSAGES.json_mode,
            variable=app.json_mode
        ).pack(side="left", padx=10)

        ttk.Button(
            bottom, text=MESSAGES.summary_button, width=12,
            command=lambda: app.show("Summary")
        ).pack(side="right", padx=10)

    def _choose(self, code):
        self.app.current_pill = code
        self.app.show("Quantity")
