import customtkinter as ctk
from config import PILLS
from messages import MESSAGES
from style import FONT_SUBTITLE, FONT_NORMAL, BTN_WIDTH, BTN_HEIGHT, MAIN_GREEN, HOVER_GREEN
from screens.components.buttons import OutlinedButton

class SelectMed(ctk.CTkFrame):

    def __init__(self, parent, app):
        super().__init__(parent, fg_color="transparent")
        self.app = app

        ctk.CTkLabel(
            self,
            text=MESSAGES.select_med_title,
            font=FONT_SUBTITLE,
            anchor="center"
        ).pack(pady=14)

        # table
        grid = ctk.CTkFrame(self, fg_color="transparent")
        grid.pack(pady=12)

        sorted_items = sorted(PILLS.items(), key=lambda kv: kv[1]["name"])
        for idx, (code, meta) in enumerate(sorted_items):
            row, col = divmod(idx, 4)
            self.select_med_btn = OutlinedButton(
                grid,
                text=meta["name"],
                width=160, height=54,
                command=lambda c=code: self._choose(c)
            ).grid(row=row, column=col, padx=12, pady=8)

        # Bottom bar
        bar = ctk.CTkFrame(self, fg_color="transparent")
        bar.pack(fill="x", pady=12)

        self.summary_btn = OutlinedButton(
            bar,
            text=MESSAGES.summary_button,
            command=lambda: app.show("Summary")
        ).grid(row=1, column=0, pady=(10, 0), sticky="s")

    def _choose(self, code):
        self.app.current_pill = code
        self.app.show("Quantity")
