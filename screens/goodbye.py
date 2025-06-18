import customtkinter as ctk
from messages import MESSAGES
from style import FONT_TITLE, BTN_WIDTH, BTN_HEIGHT, MAIN_GREEN, HOVER_GREEN

class Goodbye(ctk.CTkFrame):
    def __init__(self, parent, app):
        super().__init__(parent, fg_color="transparent")
        self.app = app

        ctk.CTkLabel(
            self,
            text=MESSAGES.goodbye_title,
            font=FONT_TITLE,
            text_color=MAIN_GREEN,
            anchor="center"
        ).pack(pady=80)

        ctk.CTkButton(
            self,
            text=MESSAGES.back_main,
            width=BTN_WIDTH,
            height=BTN_HEIGHT,
            font=("Arial", 18),
            fg_color="#222",
            hover_color=MAIN_GREEN,
            command=lambda: app.show("Welcome")
        ).pack(pady=8)

        self._return_id = self.after(3000, lambda: app.show("Welcome"))

    def cancel_timer(self):
        if getattr(self, "_return_id", None):
            self.after_cancel(self._return_id)
            self._return_id = None