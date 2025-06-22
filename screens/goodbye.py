import customtkinter as ctk
from messages import MESSAGES
from screens.components.buttons import OutlinedButton
from style import FONT_TITLE, BTN_WIDTH, BTN_HEIGHT, MAIN_GREEN, HOVER_GREEN, centered_container


class Goodbye(ctk.CTkFrame):
    def __init__(self, parent, app):
        super().__init__(parent, fg_color="transparent")
        self.app = app
        self._timer = None

        center = centered_container(self, row_weights=(0, 1, 2))

        self.label = ctk.CTkLabel(
            center,
            text=MESSAGES.goodbye_title,
            font=FONT_TITLE,
            text_color=MAIN_GREEN,
        )

        self.back_btn = OutlinedButton(
            center,
            text=MESSAGES.cancel_btn,
            command=lambda: app.show("Welcome")
        )

        self.label.grid(row=0, column=0, padx=10, pady=10)
        self.back_btn.grid(row=1, column=0, padx=10, pady=10)

        self._timer = self.after(3000, lambda: app.show("Welcome"))

    def cancel_timer(self):
        if self._timer:
            self.after_cancel(self._timer)
            self._timer = None
