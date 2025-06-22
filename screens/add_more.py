import customtkinter as ctk
from config import PILLS
from messages import MESSAGES
from style import (
    FONT_NORMAL, FONT_SUBTITLE,
    BTN_WIDTH, BTN_HEIGHT,
    MAIN_GREEN, HOVER_GREEN, centered_container, MAIN_GREY, HOVER_GREY
)
from screens.components.order_preview import render_order
from screens.components.buttons import OutlinedButton

class AddMore(ctk.CTkFrame):

    def __init__(self, parent, app):
        super().__init__(parent, fg_color="transparent")
        self.app = app

        center = centered_container(self, row_weights=(0, 1, 2, 3))
        btns = ctk.CTkFrame(center, fg_color="transparent")
        btns.grid(row=2, column=0)

        self.label = ctk.CTkLabel(
            center,
            text=MESSAGES.add_more_title,
            font=FONT_SUBTITLE,
        )

        self.noBtn = OutlinedButton(
            btns,
            text=MESSAGES.add_more_no,
            command=lambda: app.show("Summary")
        )

        self.yesBtn = OutlinedButton(
            btns,
            text=MESSAGES.add_more_yes,
            command=lambda: app.show("SelectMed")
        )

        self.label.grid(row=0, column=0)

        self.box = ctk.CTkFrame(center, fg_color="transparent")
        self.box.grid(row=1, column=0, pady=6)

        self.noBtn.grid(row=2, column=0, padx=10, pady=10)
        self.yesBtn.grid(row=2, column=1, padx=10, pady=10)

        self.cmd_label = ctk.CTkLabel(center, text="", font=FONT_NORMAL)
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