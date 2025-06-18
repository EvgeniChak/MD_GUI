import customtkinter as ctk
from messages import MESSAGES
from style import FONT_SUBTITLE, FONT_MEDIUM, BTN_WIDTH, BTN_HEIGHT, MAIN_GREEN, HOVER_GREEN

class NameInput(ctk.CTkFrame):

    def __init__(self, parent, app):
        super().__init__(parent, fg_color="transparent")
        self.app = app

        ctk.CTkLabel(
            self,
            text=MESSAGES.name_title,
            font=FONT_SUBTITLE,
            anchor="center"
        ).pack(pady=40)

        self.name_var = ctk.StringVar()
        entry = ctk.CTkEntry(
            self,
            textvariable=self.name_var,
            width=360,
            font=FONT_MEDIUM,
            placeholder_text=MESSAGES.name_placeholder
        )
        entry.pack()

        btn_row = ctk.CTkFrame(self, fg_color="transparent")
        btn_row.pack(pady=30)

        ctk.CTkButton(
            btn_row,
            text=MESSAGES.back_main,
            width=BTN_WIDTH // 1.6,
            height=BTN_HEIGHT,
            font=FONT_MEDIUM,
            fg_color="#222",
            hover_color="#444",
            command=lambda: app.show("Welcome")
        ).grid(row=0, column=0, padx=16)

        ctk.CTkButton(
            btn_row,
            text=MESSAGES.name_next,
            width=BTN_WIDTH // 1.6,
            height=BTN_HEIGHT,
            font=FONT_MEDIUM,
            fg_color=MAIN_GREEN,
            hover_color=HOVER_GREEN,
            command=lambda: app.show("SelectMed")
        ).grid(row=0, column=1, padx=16)
