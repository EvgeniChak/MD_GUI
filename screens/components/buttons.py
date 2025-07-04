import customtkinter as ctk
from messages import *
from style import BTN_WIDTH, BTN_HEIGHT, FONT_NORMAL, MAIN_GREEN, DEF_TEXT_COLOR


class DefButton(ctk.CTkButton):
    def __init__(self, master, text, fg=("#2d944a", "#38b457"), **kwargs):
        super().__init__(
            master,
            text=text,
            font=FONT_NORMAL,
            width=BTN_WIDTH,
            height=BTN_HEIGHT,
            fg_color=fg[0],
            hover_color=fg[1],
            text_color=DEF_TEXT_COLOR,
            corner_radius=8,
            **kwargs
        )

class OutlinedButton(ctk.CTkButton):
    def __init__(self, master, text, fg=("#222", "#666"), border=MAIN_GREEN,text_color="white", width = BTN_WIDTH, height = BTN_HEIGHT, **kwargs):
        super().__init__(
            master,
            text=text,
            font=FONT_NORMAL,
            fg_color=fg[0],
            hover_color=fg[1],
            width = width,
            height = height,
            text_color=text_color,
            bg_color= "transparent",
            border_color=border,
            border_width=2,
            corner_radius=8,
            **kwargs
        )

class CounterButton(ctk.CTkButton):
    def __init__(self, master, text, fg=("#333", "#555"), border=MAIN_GREEN,text_color="white", width = 60, height = 60, **kwargs):
        super().__init__(
            master,
            text=text,
            font=FONT_NORMAL,
            fg_color=fg[0],
            hover_color=fg[1],
            width = width,
            height = height,
            text_color=text_color,
            **kwargs
        )