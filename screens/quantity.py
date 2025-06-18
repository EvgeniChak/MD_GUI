import customtkinter as ctk
from config import PILLS
from messages import MESSAGES
from style import FONT_SUBTITLE, FONT_NORMAL, BTN_WIDTH, BTN_HEIGHT, MAIN_GREEN, HOVER_GREEN

class Quantity(ctk.CTkFrame):


    def __init__(self, parent, app):
        super().__init__(parent, fg_color="transparent")
        self.app = app
        self.qty = ctk.IntVar(value=1)

        self.label = ctk.CTkLabel(
            self,
            text="",
            font=FONT_SUBTITLE,
            anchor="center"
        )
        self.label.pack(pady=20)

        box = ctk.CTkFrame(self, fg_color="transparent")
        box.pack(pady=12)

        ctk.CTkButton(
            box, text="-", width=64, height=54, font=FONT_NORMAL,
            fg_color="#444", hover_color="#666",
            command=lambda: self._inc(-1)
        ).grid(row=0, column=0, padx=16)

        self.qty_label = ctk.CTkLabel(
            box, textvariable=self.qty, width=80,
            font=("Arial", 22, "bold"), anchor="center"
        )
        self.qty_label.grid(row=0, column=1)

        ctk.CTkButton(
            box, text="+", width=64, height=54, font=FONT_NORMAL,
            fg_color="#444", hover_color="#666",
            command=lambda: self._inc(+1)
        ).grid(row=0, column=2, padx=16)

        ctk.CTkButton(
            self,
            text=MESSAGES.ok_button,
            width=BTN_WIDTH, height=BTN_HEIGHT,
            font=FONT_NORMAL,
            fg_color=MAIN_GREEN,
            hover_color=HOVER_GREEN,
            command=self._confirm
        ).pack(pady=30)

    def tkraise(self, *args, **kwargs):
        super().tkraise(*args, **kwargs)
        pill_code = self.app.current_pill
        self.label.configure(text=f"{MESSAGES.quantity_title}\n{PILLS[pill_code]['name']}")
        self.qty.set(1)

    def _inc(self, delta):
        val = max(1, self.qty.get() + delta)
        self.qty.set(val)

    def _confirm(self):
        self.app.add_item(self.app.current_pill, self.qty.get())
        self.app.show("AddMore")
