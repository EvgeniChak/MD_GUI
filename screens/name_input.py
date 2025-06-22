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
        btns = ctk.CTkFrame(center, fg_color="transparent")
        btns.grid(row=2, column=0, pady=20)


        self.label = ctk.CTkLabel(
            center,
            text=MESSAGES.name_title,
            font=FONT_SUBTITLE,
        )

        self.entry = ctk.CTkEntry(
            center,
            textvariable=self.name_var,
            width=360,
            font=FONT_MEDIUM,
            placeholder_text=MESSAGES.name_placeholder
        )

        self.backBtn = OutlinedButton(
            btns,
            text=MESSAGES.back_main,
            command=lambda: app.show("Welcome")
        )

        self.nextBtn = OutlinedButton(
            btns,
            text=MESSAGES.name_next,
            command=lambda: app.show("SelectMed")
        )

        self.label.grid(row=0, column=0)
        self.entry.grid(row=1, column=0)
        self.backBtn.grid(row=2, column=0, padx=10)
        self.nextBtn.grid(row=2, column=1,padx=10)

    def clear(self):
        self.name_var.set("")
