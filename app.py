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
    """Background thread for UART communication."""
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
    """Main Application Window."""
    def __init__(self):
        super().__init__()
        self.title("Medical Dispenser GUI")
        self.geometry("1280x720")
        self.resizable(False, False)

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
        """Navigate to screen by name and reset inactivity timer."""
        self.screens[name].tkraise()
        self._reset_timer()

    def add_item(self, code: str, qty: int):
        """Add medication to order."""
        self.order[code] = self.order.get(code, 0) + qty

    def clear_order(self):
        """Clear current medication order."""
        self.order.clear()

    def build_serial(self) -> str:
        """Build serial command string."""
        cells = [PILLS[c]["cell"] for c, q in self.order.items() for _ in range(q)]
        return f"get({','.join(cells)})"

    def build_json(self) -> str:
        """Build JSON command string."""
        return json.dumps({
            "command": "dispense",
            "items": [{"pill": c, "quantity": q} for c, q in self.order.items()],
        }, separators=(",", ":"))

    def send_order(self):
        """Send order via serial or JSON."""
        cmd = self.build_json() if self.json_mode.get() else self.build_serial()
        self.tx_q.put(cmd)

    def _reset_timer(self):
        """Reset inactivity timer."""
        if self._timer_id:
            self.after_cancel(self._timer_id)
        self._timer_id = self.after(TIMEOUT_MS, self._timeout)

    def _timeout(self):
        """Handle inactivity timeout."""
        self.clear_order()
        messagebox.showinfo(MESSAGES.timeout_message, MESSAGES.timeout_message)
        self.show("Welcome")
