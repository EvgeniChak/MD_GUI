import customtkinter as ctk
from messages import MESSAGES

class Welcome(ctk.CTkFrame):
    """Welcome screen for the Medical Dispenser GUI."""

    def __init__(self, parent, app):
        """
        Initialize the Welcome screen.

        Args:
            parent: The parent widget (CTkFrame).
            app: The main application instance.
        """
        super().__init__(parent, fg_color="transparent")
        self.app = app

        self.label = ctk.CTkLabel(
            self,
            text=MESSAGES.welcome_title,
            font=("Arial", 26, "bold"),
            text_color="#d0ffb2",   # светло-зелёный на dark теме
            anchor="center"
        )
        self.label.pack(pady=80)

        self.start_btn = ctk.CTkButton(
            self,
            text=MESSAGES.start_button,
            width=180,
            height=48,
            font=("Arial", 20, "bold"),
            fg_color="#35af4c",        # основной зелёный
            hover_color="#56cf5b",     # чуть ярче при наведении
            command=lambda: app.show("NameInput")
        )
        self.start_btn.pack(pady=16)

        # Здесь можно добавить логотип/картинку/название компании
