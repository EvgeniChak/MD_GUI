import customtkinter as ctk
from messages import MESSAGES
from style import FONT_TITLE, BTN_WIDTH, BTN_HEIGHT, MAIN_GREEN, HOVER_GREEN

class Goodbye(ctk.CTkFrame):
    def __init__(self, parent, app):
        super().__init__(parent, fg_color="transparent")
        self.app = app
        self._timer = None

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        center = ctk.CTkFrame(self, fg_color="transparent")
        center.grid(row=0, column=0, sticky="nsew")

        center.grid_rowconfigure((0,1), weight=1)
        center.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(
            center,
            text=MESSAGES.goodbye_title,
            font=FONT_TITLE,
            text_color=MAIN_GREEN,
            anchor="center"
        ).grid(row=0, column=0, sticky="s")

        ctk.CTkButton(
            center,
            text=MESSAGES.back_main,
            width=BTN_WIDTH,
            height=BTN_HEIGHT,
            fg_color="#222",
            hover_color=MAIN_GREEN,
            command=lambda: app.show("Welcome")
        ).grid(row=1, column=0, pady=10, sticky="n")

        self._timer = self.after(3000, lambda: app.show("Welcome"))

    def cancel_timer(self):
        if self._timer:
            self.after_cancel(self._timer)
            self._timer = None
