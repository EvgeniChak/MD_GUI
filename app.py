# app.py — версия с ttkbootstrap

import json
import queue
import threading
from tkinter import messagebox  # messagebox остаётся из стандартного tkinter

import ttkbootstrap as ttkb  # главный импорт темы
from ttkbootstrap import ttk  # drop‑in ttk‑виджеты

from config import PILLS
from messages import MESSAGES
from screens import (
    Welcome,
    NameInput,
    SelectMed,
    Quantity,
    AddMore,
    Summary,
    Goodbye,
)

# === ПАРАМЕТРЫ ТЕМЫ ================================================
THEME_NAME = "cosmo"   # можно заменить на cosmo, darkly, morph и др.
TIMEOUT_MS = 30_000      # 30 с глобальный тайм‑аут
GOODBYE_MS = 3_000       # 3 с авто‑возврат с экрана Goodbye


# ---------- UART‑поток ---------------------------------------------
class SerialWorker(threading.Thread):
    def __init__(self, tx_q: queue.Queue):
        super().__init__(daemon=True)
        self.tx_q = tx_q
        try:
            import serial  # локальный импорт, чтобы не ломаться без пакета
            self.ser = serial.Serial(port="COM3", baudrate=115200, timeout=1)
        except Exception:
            self.ser = None

    def run(self):
        while True:
            cmd = self.tx_q.get()
            print(">>>", cmd)
            if self.ser:
                self.ser.write(cmd.encode() + b"\r\n")


# ---------- Главное приложение -------------------------------------
class MDApp(ttkb.Window):  # наследуемся от themed Window
    def __init__(self):
        super().__init__(themename=THEME_NAME)

        # базовые атрибуты окна
        self.title("Medical Dispenser GUI")
        self.geometry("900x550")
        self.resizable(False, False)

        # состояние заказа
        self.order: dict[str, int] = {}
        self.current_pill: str | None = None
        self.json_mode = ttkb.BooleanVar(value=False)

        # таймер бездействия
        self._timer_id: str | None = None

        # очередь TX + UART‑поток
        self.tx_q: queue.Queue[str] = queue.Queue()
        SerialWorker(self.tx_q).start()

        # контейнер экранов
        container = ttkb.Frame(self)
        container.pack(fill="both", expand=True)

        self.screens = {}
        for Scr in (
            Welcome,
            NameInput,
            SelectMed,
            Quantity,
            AddMore,
            Summary,
            Goodbye,
        ):
            scr = Scr(parent=container, app=self)
            self.screens[Scr.__name__] = scr
            scr.grid(row=0, column=0, sticky="nsew")

        self.show("Welcome")

    # --- Навигация между экранами ----------------------------------
    def show(self, name: str):
        self.screens[name].tkraise()
        self._reset_timer()

    # --- Работа с заказом ------------------------------------------
    def add_item(self, code: str, qty: int):
        self.order[code] = self.order.get(code, 0) + qty

    def clear_order(self):
        self.order.clear()

    def build_serial(self) -> str:
        cells = [PILLS[c]["cell"] for c, q in self.order.items() for _ in range(q)]
        return f"get({','.join(cells)})"

    def build_json(self) -> str:
        return json.dumps({
            "command": "dispense",
            "items": [{"pill": c, "quantity": q} for c, q in self.order.items()],
        }, separators=(",", ":"))

    def send_order(self):
        cmd = self.build_json() if self.json_mode.get() else self.build_serial()
        self.tx_q.put(cmd)

    # --- Тайм‑аут ---------------------------------------------------
    def _reset_timer(self):
        if self._timer_id:
            self.after_cancel(self._timer_id)
        self._timer_id = self.after(TIMEOUT_MS, self._timeout)

    def _timeout(self):
        self.clear_order()
        messagebox.showinfo(MESSAGES.timeout_message, MESSAGES.timeout_message)
        self.show("Welcome")

