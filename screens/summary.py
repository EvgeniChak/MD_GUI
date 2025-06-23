import customtkinter as ctk
from config import PILLS
from messages import MESSAGES
from screens.components.buttons import OutlinedButton
from style import FONT_SUBTITLE, FONT_NORMAL, BTN_WIDTH, BTN_HEIGHT, MAIN_GREEN, HOVER_GREEN, centered_container
from screens.components.order_preview import render_order

class Summary(ctk.CTkFrame):

    def __init__(self, parent, app):
        super().__init__(parent, fg_color="transparent")
        self.app = app

        center = centered_container(self, row_weights=(0, 1, 2, 3))
        btns = ctk.CTkFrame(center, fg_color="transparent")
        btns.grid(row=2, column=0, pady=16)

        self.label= ctk.CTkLabel(
            center,
            text=MESSAGES.summary_title,
            font=FONT_SUBTITLE,
        )

        self.cancel_btn = OutlinedButton(
            btns,
            text=MESSAGES.cancel_btn,
            command=self._cancel
        )

        self.send_btn = OutlinedButton(
            btns,
            text=MESSAGES.send_btn,
            command=self._send
        )


        self.box = ctk.CTkFrame(center, fg_color="transparent")
        self.cmd_label = ctk.CTkLabel(center, text="", font=FONT_NORMAL)

        self.label.grid(row=0, column=0, pady=10, sticky="s")
        self.box.grid(row=1, column=0, pady=6)
        self.cancel_btn.grid(row=1, column=0, pady=10)
        self.send_btn.grid(row=1, column=1, padx=20)

        self.cmd_label.grid(row=3, column=0, pady=10, padx=10,sticky="SW")




    def tkraise(self, *args, **kwargs):
        super().tkraise(*args, **kwargs)
        cmd = (
            self.app.build_json()
            if self.app.json_mode.get()
            else self.app.build_serial()
        )
        render_order(self.box, self.app.order)
        self.cmd_label.configure(text=cmd)

    def _send(self):
        self.app.send_order()
        self.app.clear_order()
        self.app.show("Goodbye")

    def _cancel(self):
        self.app.clear_order()
        self.app.show("Welcome")

    def _build_cmd(self) -> str:
        return (
            self.app.build_json()
            if self.app.json_mode.get()
            else self.app.build_serial()
        )