import customtkinter as ctk
from config import PILLS
from messages import MESSAGES
from style import FONT_SUBTITLE, FONT_NORMAL, BTN_WIDTH, BTN_HEIGHT, MAIN_GREEN, HOVER_GREEN, centered_container

from screens.components.buttons import OutlinedButton, CounterButton


class Quantity(ctk.CTkFrame):


    def __init__(self, parent, app):
        super().__init__(parent, fg_color="transparent")
        self.app = app
        self.qty = ctk.IntVar(value=1)

        center = centered_container(self, row_weights=(0, 1, 2, 3))

        counter = ctk.CTkFrame(center, fg_color="transparent")
        counter.grid(row=1, column=0)

        counter.grid_columnconfigure((0, 1, 2), weight=1)

        self.label = ctk.CTkLabel(
            center,
            text="",
            font=FONT_SUBTITLE,
        )

        self.minusBtn = CounterButton(
            counter,
            text=MESSAGES.minus_button,
            command=lambda: self._inc(-1)
        )

        self.plusBtn = CounterButton(
            counter,
            text=MESSAGES.plus_button,
            command=lambda: self._inc(1)
        )
        self.qtyLabel = ctk.CTkLabel(
            counter,
            textvariable=self.qty,
            font=("Arial", 22, "bold"),
            width=60,
        )

        self.okBtn = OutlinedButton(
            center,
            text=MESSAGES.ok_button,
            command=self._confirm
        )

        self.label.grid(row=0, column=0, padx=10)
        self.minusBtn.grid(row=1, column=0, padx=10)
        self.qtyLabel.grid(row=1, column=1)
        self.plusBtn.grid(row=1, column=2, padx=10)
        self.okBtn.grid(row=2, column=0)


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
