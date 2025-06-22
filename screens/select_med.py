import customtkinter as ctk
from config import PILLS
from messages import MESSAGES
from style import (
    FONT_SUBTITLE, FONT_NORMAL,
    BTN_WIDTH, BTN_HEIGHT,
    MAIN_GREEN, HOVER_GREEN,
    centered_container
)
from screens.components.buttons import OutlinedButton


class SelectMed(ctk.CTkFrame):
    def __init__(self, parent, app):
        super().__init__(parent, fg_color="transparent")
        self.app = app

        center = centered_container(self, row_weights=(0, 1, 2))

        self.label =ctk.CTkLabel(
            center,
            text=MESSAGES.select_med_title,
            font=FONT_SUBTITLE,
            anchor="center"
        )

        self.summaryBtn = OutlinedButton(
            center,
            text=MESSAGES.summary_button,
            command=lambda: app.show("Summary")
        )

        self.grid_frame = ctk.CTkFrame(center, fg_color="transparent")
        self.grid_frame.grid(row=1, column=0, pady=(0, 10))

        sorted_items = sorted(PILLS.items(), key=lambda kv: kv[1]["name"])

        for idx, (code, meta) in enumerate(sorted_items):
            row, col = divmod(idx, 4)
            btn = OutlinedButton(
                self.grid_frame,
                text=meta["name"],
                width=160,
                height=54,
                command=lambda c=code: self._choose(c)
            )
            btn.grid(row=row, column=col, padx=10, pady=6)


        self.label.grid(row=0, column=0, pady=10)
        self.summaryBtn.grid(row=2, column=0, pady=10, sticky="n")


    def _choose(self, code: str):
        self.app.current_pill = code
        self.app.show("Quantity")
