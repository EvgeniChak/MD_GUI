import customtkinter as ctk
from messages import MESSAGES
from style import (
    FONT_SUBTITLE, FONT_MEDIUM,
    BTN_WIDTH, BTN_HEIGHT,
    MAIN_GREEN, HOVER_GREEN, centered_container
)
from screens.components.buttons import OutlinedButton

class NameInput(ctk.CTkFrame):

    def __init__(self, parent, app):
        super().__init__(parent, fg_color="transparent")
        self.app = app
        self.name_var = ctk.StringVar()

        center = centered_container(self, row_weights=(0, 1, 2, 3))

        ctk.CTkLabel(
            center,
            text=MESSAGES.name_title,
            font=FONT_SUBTITLE,
            anchor="center"
        ).grid(row=0, column=0, pady=(0, 12), sticky="s")

        self.entry = ctk.CTkEntry(
            center,
            textvariable=self.name_var,
            width=360,
            font=FONT_MEDIUM,
            placeholder_text=MESSAGES.name_placeholder
        )
        self.entry.grid(row=1, column=0, pady=6)

        btns = ctk.CTkFrame(center, fg_color="transparent")
        btns.grid(row=2, column=0, pady=20)

        self.back_btn = OutlinedButton(
            btns,
            text=MESSAGES.back_main,
            command=lambda: app.show("Welcome")
        ).grid(row=0, column=0, padx=16)

        self.next_btn = OutlinedButton(
            btns,
            text=MESSAGES.name_next,
            command=lambda: app.show("SelectMed")
        ).grid(row=0, column=1, padx=16)

    def clear(self):
        self.name_var.set("")
