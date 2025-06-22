import customtkinter as ctk
from config import PILLS
from style import FONT_NORMAL, FONT_SUBTITLE, MAIN_GREEN


def render_order(
    parent: ctk.CTkFrame,
    order: dict[str, int],
    show_cmd: bool = False,
    cmd: str = "",
    allow_delete: bool = False,
    on_delete: callable = None
):

    for w in parent.winfo_children():
        w.destroy()


    for i, (code, qty) in enumerate(order.items(), 1):
        name = PILLS[code]["name"]
        row = i - 1

        ctk.CTkLabel(
            parent,
            text=f"{i}. {name}",
            font=FONT_NORMAL,
            anchor="w",
            width=200
        ).grid(row=row, column=0, sticky="w")

        ctk.CTkLabel(
            parent,
            text=f"×{qty}",
            font=FONT_NORMAL,
            width=40
        ).grid(row=row, column=1)

        if allow_delete and on_delete:
            ctk.CTkButton(
                parent,
                text="✕",
                width=28, height=28,
                fg_color="#911",
                hover_color="#c33",
                font=("Arial", 16),
                command=lambda c=code: on_delete(c)
            ).grid(row=row, column=3, padx=(6, 0))


    if show_cmd:
        ctk.CTkLabel(
            parent,
            text=cmd,
            font=FONT_NORMAL,
            anchor="center"
        ).grid(row=i + 1, column=0, columnspan=4, pady=6)
