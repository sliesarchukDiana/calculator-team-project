import tkinter as tk
from tkinter import messagebox
import logging
import os

logging.basicConfig(
    filename="Session log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)
logging.info("=== Нова сесія запущена ===")

class CalculatorApp:
    def __init__(self, master):
        self.master = master
        master.title("Арифметичний калькулятор")
        master.geometry("400x300")

        self.num1 = tk.DoubleVar()
        self.num2 = tk.DoubleVar()
        self.operation = tk.StringVar(value="+")

        tk.Label(master, text="Перше число:").pack()
        tk.Entry(master, textvariable=self.num1).pack()

        tk.Label(master, text="Друге число:").pack()
        tk.Entry(master, textvariable=self.num2).pack()

        tk.Label(master, text="Оберіть операцію:").pack()

        frame = tk.Frame(master)
        frame.pack()
        for op in ["+", "-", "*", "/", "**"]:
            tk.Radiobutton(frame, text=op, value=op, variable=self.operation).pack(side="left")

        tk.Button(master, text="Імпортувати дані", command=self.import_data).pack(pady=3)
        tk.Button(master, text="Обчислити", command=self.calculate).pack(pady=3)
        tk.Button(master, text="Експортувати результат", command=self.export_result).pack(pady=3)

        self.result_label = tk.Label(master, text="Результат: ", font=("Arial", 12))
        self.result_label.pack(pady=10)

        self.result = None
        self.input_path = "Input data.txt"
        self.output_path = "Output data.txt"

        # Add import/export data, calculate functions
if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.protocol("WM_DELETE_WINDOW", lambda: (logging.info("=== Сесію завершено ==="), root.destroy()))
    root.mainloop()
