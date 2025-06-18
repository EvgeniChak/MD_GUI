import customtkinter as ctk
from messages import MESSAGES
from style import FONT_TITLE, BTN_WIDTH, BTN_HEIGHT, MAIN_GREEN, HOVER_GREEN, TEXT_GREEN

class Welcome(ctk.CTkFrame):
    """Welcome screen for the Medical Dispenser GUI."""

    def __init__(self, parent, app):
        super().__init__(parent, fg_color="transparent")
        self.app = app

        ctk.CTkLabel(
            self,
            text=MESSAGES.welcome_title,
            font=FONT_TITLE,
            text_color=TEXT_GREEN,
            anchor="center"
        ).pack(pady=80)

        ctk.CTkButton(
            self,
            text=MESSAGES.start_button,
            width=BTN_WIDTH,
            height=BTN_HEIGHT,
            font=("Arial", 20, "bold"),
            fg_color=MAIN_GREEN,
            hover_color=HOVER_GREEN,
            command=lambda: app.show("NameInput")
        ).pack(pady=16)
