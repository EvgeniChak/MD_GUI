import customtkinter as ctk
from messages import MESSAGES
from style import FONT_TITLE, BTN_WIDTH, BTN_HEIGHT, MAIN_GREEN, HOVER_GREEN, TEXT_GREEN

class Welcome(ctk.CTkFrame):
    def __init__(self, parent, app):
        super().__init__(parent, fg_color="transparent")
        self.app = app

        center = ctk.CTkFrame(self, fg_color="transparent")
        center.pack(expand=True, fill="both")

        label = ctk.CTkLabel(
            center,
            text=MESSAGES.welcome_title,
            font=FONT_TITLE,
            text_color=TEXT_GREEN,
            anchor="center"
        )
        label.place(relx=0.5, rely=0.45, anchor="center")

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
