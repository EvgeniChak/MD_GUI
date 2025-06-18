import customtkinter as ctk
from messages import MESSAGES
from style import (
    FONT_TITLE, BTN_WIDTH, BTN_HEIGHT,
    MAIN_GREEN, HOVER_GREEN, TEXT_GREEN
)

class Welcome(ctk.CTkFrame):
    def __init__(self, parent, app):
        super().__init__(parent, fg_color="transparent")
        self.app = app

        # 1) делаем ячейку 0×0 растягиваемой
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # 2) центральный контейнер
        center = ctk.CTkFrame(self, fg_color="transparent")
        center.grid(row=0, column=0, sticky="nsew")

        # 3) контент по центру
        center.grid_rowconfigure((0, 1), weight=1)
        center.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(
            center,
            text=MESSAGES.welcome_title,
            font=FONT_TITLE,
            text_color=TEXT_GREEN
        ).grid(row=0, column=0, sticky="s")

        ctk.CTkButton(
            center,
            text=MESSAGES.start_btn,
            width=BTN_WIDTH,
            height=BTN_HEIGHT,
            font=("Arial", 20, "bold"),
            fg_color=MAIN_GREEN,
            hover_color=HOVER_GREEN,
            command=lambda: app.show("NameInput")
        ).grid(row=1, column=0, pady=20, sticky="n")
