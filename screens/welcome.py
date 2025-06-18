import customtkinter as ctk
from messages import MESSAGES
from style import (
    FONT_TITLE, BTN_WIDTH, BTN_HEIGHT,
    MAIN_GREEN, HOVER_GREEN, TEXT_GREEN, centered_container
)

class Welcome(ctk.CTkFrame):
    def __init__(self, parent, app):
        super().__init__(parent, fg_color="transparent")
        self.app = app

        center = centered_container(self, row_weights=(0, 1, 2))

        ctk.CTkLabel(
            center,
            text=MESSAGES.welcome_title,
            font=FONT_TITLE
        ).grid(row=0, column=0, pady=(0, 10), sticky="s")

        ctk.CTkButton(
            center,
            text=MESSAGES.start_btn,
            command=lambda: app.show("NameInput")
        ).grid(row=1, column=0, pady=(0, 10), sticky="")

        ctk.CTkCheckBox(
            center,
            text=MESSAGES.json_mode,
            variable=app.json_mode
        ).grid(row=2, column=0, pady=(10, 0))