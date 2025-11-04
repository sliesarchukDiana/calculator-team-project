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
    def import_data(self):
        if not os.path.exists(self.input_path):
            messagebox.showerror("Помилка", f"Файл {self.input_path} не знайдено.")
            return

        try:
            with open(self.input_path, "r", encoding="utf-8") as f:
                line = f.readline().strip()
                parts = line.replace(",", " ").split()
                if len(parts) >= 2:
                    self.num1.set(float(parts[0]))
                    self.num2.set(float(parts[1]))
                    messagebox.showinfo("Імпорт", f"Дані імпортовано: {parts[0]}, {parts[1]}")
                    logging.info(f"Імпортовано дані: {parts}")
                else:
                    raise ValueError("Недостатньо параметрів у файлі.")
        except Exception as e:
            messagebox.showerror("Помилка", str(e))
    def calculate(self):
            a = self.num1.get()
            b = self.num2.get()
            op = self.operation.get()
            try:
                if op == "+":
                    self.result = a + b
                elif op == "-":
                    self.result = a - b
                elif op == "*":
                    self.result = a * b
                elif op == "/":
                    if b == 0:
                        raise ZeroDivisionError("Ділення на нуль")
                    self.result = a / b
                elif op == "**":
                    self.result = a ** b
                else:
                    raise ValueError("Невідома операція")

                self.result_label.config(text=f"Результат: {self.result}")
                logging.info(f"Виконано: {a} {op} {b} = {self.result}")

            except Exception as e:
                messagebox.showerror("Помилка", str(e))
                logging.error(f"Помилка обчислення: {e}")
    def export_result(self):
        if self.result is None:
            messagebox.showwarning("Увага", "Спочатку виконайте обчислення.")
            return

        with open(self.output_path, "a", encoding="utf-8") as f:
            line = f"{self.num1.get()} {self.operation.get()} {self.num2.get()}, Результат: {self.result}\n"
            f.write(line)
        messagebox.showinfo("Експорт", "Результат збережено у Output data.txt")
        logging.info(f"Експортовано результат: {line.strip()}")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.protocol("WM_DELETE_WINDOW", lambda: (logging.info("=== Сесію завершено ==="), root.destroy()))
    root.mainloop()
