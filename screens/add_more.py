import customtkinter as ctk
from messages import MESSAGES
from style import FONT_SUBTITLE, FONT_NORMAL, BTN_WIDTH, BTN_HEIGHT, MAIN_GREEN, HOVER_GREEN, centered_container

class AddMore(ctk.CTkFrame):


    def __init__(self, parent, app):
        super().__init__(parent, fg_color="transparent")
        self.app = app

        center = centered_container(self, row_weights=(0, 1, 2))

        ctk.CTkLabel(
            center,
            text=MESSAGES.add_more_title,
            font=FONT_SUBTITLE,

        ).grid(row=0, column=0)

        btns = ctk.CTkFrame(center, fg_color="transparent")
        btns.grid(row=1, column=0)

        ctk.CTkButton(
            btns,
            text=MESSAGES.add_more_no,
            width=BTN_WIDTH,
            height=BTN_HEIGHT,
            font=FONT_NORMAL,
            fg_color=MAIN_GREEN,
            hover_color=HOVER_GREEN,
            command=lambda: app.show("Summary")
        ).grid(row=0, column=0, padx=30)

        ctk.CTkButton(
            btns,
            text=MESSAGES.add_more_yes,
            width=BTN_WIDTH,
            height=BTN_HEIGHT,
            font=FONT_NORMAL,
            fg_color=MAIN_GREEN,
            hover_color=HOVER_GREEN,
            command=lambda: app.show("SelectMed")
        ).grid(row=0, column=1, padx=30)


