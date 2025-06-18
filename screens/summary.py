import customtkinter as ctk
from config import PILLS
from messages import MESSAGES
from style import FONT_SUBTITLE, FONT_NORMAL, BTN_WIDTH, BTN_HEIGHT, MAIN_GREEN, HOVER_GREEN, centered_container

class Summary(ctk.CTkFrame):

    def __init__(self, parent, app):
        super().__init__(parent, fg_color="transparent")
        self.app = app

        center = centered_container(self, row_weights=(0, 1, 2, 3))

        ctk.CTkLabel(
            center,
            text=MESSAGES.summary_title,
            font=FONT_SUBTITLE,
            anchor="center"
        ).grid(row=0, column=0, pady=10, sticky="s")

        # Блок списка заказов
        self.box = ctk.CTkFrame(center, fg_color="transparent")
        self.box.grid(row=1, column=0, pady=6)

        # Кнопки отправки и отмены
        btns = ctk.CTkFrame(center, fg_color="transparent")
        btns.grid(row=2, column=0, pady=16)

        ctk.CTkButton(
            btns,
            text=MESSAGES.cancel_btn,
            width=BTN_WIDTH,
            height=BTN_HEIGHT,
            font=FONT_NORMAL,
            fg_color="#222",
            hover_color="#444",
            command=self._cancel
        ).grid(row=0, column=0, padx=20)

        ctk.CTkButton(
            btns,
            text=MESSAGES.send_btn,
            width=BTN_WIDTH,
            height=BTN_HEIGHT,
            font=FONT_NORMAL,
            fg_color=MAIN_GREEN,
            hover_color=HOVER_GREEN,
            command=self._send
        ).grid(row=0, column=1, padx=20)

        # Строка с командой (json/serial)
        self.cmd_label = ctk.CTkLabel(center, text="", font=FONT_NORMAL)
        self.cmd_label.grid(row=3, column=0, pady=10)



    def tkraise(self, *args, **kwargs):
        super().tkraise(*args, **kwargs)
        # Clear box
        for w in self.box.winfo_children():
            w.destroy()

        for i, (code, qty) in enumerate(self.app.order.items(), 1):
            ctk.CTkLabel(
                self.box,
                text=f"{i}. {PILLS[code]['name']}",
                width=220, font=FONT_NORMAL, anchor="w"
            ).grid(row=i, column=0, sticky="w")
            ctk.CTkLabel(
                self.box, text=f"×{qty}", width=60, font=FONT_NORMAL
            ).grid(row=i, column=1, sticky="e")

        cmd = (
            self.app.build_json()
            if self.app.json_mode.get()
            else self.app.build_serial()
        )
        self.cmd_label.configure(text=cmd)

    def _send(self):
        self.app.send_order()
        self.app.show("Goodbye")

    def _cancel(self):
        self.app.clear_order()
        self.app.show("Welcome")
