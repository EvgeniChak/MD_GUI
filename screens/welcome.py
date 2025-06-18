import customtkinter as ctk
from messages import MESSAGES
from style import FONT_TITLE, BTN_WIDTH, BTN_HEIGHT, MAIN_GREEN, HOVER_GREEN, TEXT_GREEN

class Welcome(ctk.CTkFrame):
    """Welcome screen for the Medical Dispenser GUI."""

    def __init__(self, parent, app):
        super().__init__(parent, fg_color="transparent")
        self.app = app

        # 1. Создай фрейм-контейнер, который заполняет всё пространство
        center = ctk.CTkFrame(self, fg_color="transparent")
        center.pack(expand=True, fill="both")

        # 2. Центруем всё в этом фрейме с помощью .place(relx, rely, anchor)
        label = ctk.CTkLabel(
            center,
            text=MESSAGES.welcome_title,
            font=FONT_TITLE,
            text_color=TEXT_GREEN,
            anchor="center"
        )
        label.place(relx=0.5, rely=0.4, anchor="center")

        start_btn = ctk.CTkButton(
            center,
            text=MESSAGES.start_btn,
            width=BTN_WIDTH,
            height=BTN_HEIGHT,
            font=("Arial", 20, "bold"),
            fg_color=MAIN_GREEN,
            hover_color=HOVER_GREEN,
            command=lambda: app.show("NameInput")
        )
        start_btn.place(relx=0.5, rely=0.6, anchor="center")
