import customtkinter as ctk
import json
import queue
import threading
from tkinter import messagebox

from config import PILLS
from messages import MESSAGES
from style import (MAIN_GREEN, HOVER_GREEN)
from screens import (
    Welcome,
    NameInput,
    SelectMed,
    Quantity,
    AddMore,
    Summary,
    Goodbye,
)

TIMEOUT_MS = 30_000
GOODBYE_MS = 3_000

class SerialWorker(threading.Thread):

    def __init__(self, tx_q: queue.Queue):
        super().__init__(daemon=True)
        self.tx_q = tx_q
        try:
            import serial
            self.ser = serial.Serial(port="COM3", baudrate=115200, timeout=1)
        except Exception:
            self.ser = None

    def run(self):
        while True:
            cmd = self.tx_q.get()
            print(">>>", cmd)
            if self.ser:
                self.ser.write(cmd.encode() + b"\r\n")

class MDApp(ctk.CTk):

    def __init__(self):
        super().__init__()
        self.title("Medical Dispenser GUI")
        self.geometry("700x350")
        self.resizable(True, True)

        self.order: dict[str, int] = {}
        self.current_pill: str | None = None
        self.json_mode = ctk.BooleanVar(value=False)
        self._timer_id: str | None = None
        self.tx_q: queue.Queue[str] = queue.Queue()
        SerialWorker(self.tx_q).start()

        container = ctk.CTkFrame(self, fg_color="transparent")
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

    def show(self, name: str):

        if self._timer_id:
            self.after_cancel(self._timer_id)
            self._timer_id = None

        if hasattr(self.screens.get("Goodbye"), "cancel_timer"):
            self.screens["Goodbye"].cancel_timer()
        self.screens[name].tkraise()
        self._reset_timer()

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

    def _reset_timer(self):
        if self._timer_id:
            self.after_cancel(self._timer_id)
        self._timer_id = self.after(TIMEOUT_MS, self._timeout)

    def _timeout(self):
        self.clear_order()
        messagebox.showinfo(MESSAGES.timeout_message, MESSAGES.timeout_message)
        self.show("Welcome")
