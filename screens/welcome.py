import customtkinter as ctk
from messages import MESSAGES
from style import (
    FONT_TITLE, BTN_WIDTH, BTN_HEIGHT,
    MAIN_GREEN, HOVER_GREEN, TEXT_GREEN, centered_container, FONT_NORMAL
)
from screens.components.buttons import OutlinedButton

class Welcome(ctk.CTkFrame):
    def __init__(self, parent, app):
        super().__init__(parent, fg_color="transparent")
        self.app = app

        center = centered_container(self, row_weights=(0, 1, 2))

        self.label = ctk.CTkLabel(
            center,
            text=MESSAGES.welcome_title,
            font=FONT_TITLE
        )
        self.start_button = OutlinedButton(
            center,
            text=MESSAGES.start_btn,
            command=lambda: app.show("NameInput")
        )

        self.checkBox = ctk.CTkCheckBox(
            center,
            text=MESSAGES.json_mode,
            variable=app.json_mode
        )

        self.label.grid(row=0, column=0, pady=20)
        self.start_button.grid(row=1, column=0, pady=10)
        self.checkBox.grid(row=2, column=0, pady=10, padx=10,sticky="SW")
