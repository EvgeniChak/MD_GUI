import json, queue, threading, tkinter as tk
from tkinter import messagebox
try:
    import serial
except ModuleNotFoundError:
    serial = None

from config import PILLS
from messages import MESSAGES
from screens import (
    Welcome, NameInput, SelectMed,
    Quantity, AddMore, Summary, Goodbye
)

TIMEOUT_MS = 30_000      # 30 с глобальный тайм-аут
GOODBYE_MS = 3_000       # 3 с автопереход с Goodbye

# ---------- UART поток ----------
class SerialWorker(threading.Thread):
    def __init__(self, tx_q: queue.Queue):
        super().__init__(daemon=True)
        self.tx_q = tx_q
        self.ser = None
        if serial:
            try:
                self.ser = serial.Serial(port="COM3", baudrate=115200, timeout=1)
            except serial.SerialException:
                pass

    def run(self):
        while True:
            cmd = self.tx_q.get()
            print(">>>", cmd)
            if self.ser:
                self.ser.write(cmd.encode() + b"\r\n")

# ---------- Главное приложение ----------
class MDApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Medical Dispenser GUI")
        self.geometry("900x550")
        self.configure(background="white")
        self.resizable(False, False)

        # состояние
        self.order: dict[str, int] = {}
        self.current_pill: str | None = None
        self.json_mode = tk.BooleanVar(value=False)

        # таймер
        self._timer_id: str | None = None

        # очередь TX
        self.tx_q: queue.Queue[str] = queue.Queue()
        SerialWorker(self.tx_q).start()

        # контейнер для экранов
        container = tk.Frame(self, bg="white")
        container.pack(fill="both", expand=True)

        self.screens = {}
        for Scr in (
            Welcome, NameInput, SelectMed,
            Quantity, AddMore, Summary, Goodbye
        ):
            scr = Scr(parent=container, app=self)
            self.screens[Scr.__name__] = scr
            scr.grid(row=0, column=0, sticky="nsew")

        self.show("Welcome")

    # ---------- навигация ----------
    def show(self, name: str):
        self.screens[name].tkraise()
        self._reset_timer()

    # ---------- заказ ----------
    def add_item(self, code: str, qty: int):
        self.order[code] = self.order.get(code, 0) + qty

    def clear_order(self):
        self.order.clear()

    def build_serial(self) -> str:
        cells = [
            PILLS[c]["cell"] for c, q in self.order.items() for _ in range(q)
        ]
        return f"get({','.join(cells)})"

    def build_json(self) -> str:
        return json.dumps({
            "command": "dispense",
            "items": [{"pill": c, "quantity": q} for c, q in self.order.items()]
        }, separators=(",", ":"))

    def send_order(self):
        cmd = self.build_json() if self.json_mode.get() else self.build_serial()
        self.tx_q.put(cmd)

    # ---------- тайм-аут ----------
    def _reset_timer(self):
        if self._timer_id:
            self.after_cancel(self._timer_id)
        self._timer_id = self.after(TIMEOUT_MS, self._timeout)

    def _timeout(self):
        self.clear_order()
        self.after_cancel(self._timer_id)
        messagebox.showinfo(MESSAGES.timeout_message, MESSAGES.timeout_message)
        self.show("Welcome")
