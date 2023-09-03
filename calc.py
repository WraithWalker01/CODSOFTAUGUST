import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("300x400")

        self.create_widgets()

    def create_widgets(self):
        self.entry_num1 = ttk.Entry(self.root, font=("Helvetica", 18))
        self.entry_num2 = ttk.Entry(self.root, font=("Helvetica", 18))

        self.create_number_buttons()
        self.create_operation_buttons()

        self.calculate_button = ttk.Button(self.root, text="Calculate", command=self.calculate)
        self.result_label = ttk.Label(self.root, text="Result:", font=("Helvetica", 18))

        self.arrange_widgets()

    def create_number_buttons(self):
        self.number_buttons = []
        for i in range(10):
            number_button = ttk.Button(self.root, text=str(i), command=lambda i=i: self.add_number(i))
            self.number_buttons.append(number_button)

    def create_operation_buttons(self):
        self.operation_buttons = []
        for operation in ["+", "-", "*", "/", "^"]:
            operation_button = ttk.Button(self.root, text=operation, command=lambda operation=operation: self.add_operation(operation))
            self.operation_buttons.append(operation_button)

    def arrange_widgets(self):
        self.entry_num1.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        self.entry_num2.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

        row = 2
        col = 0
        for button in self.number_buttons:
            button.grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col > 2:
                col = 0
                row += 1

        row += 1
        col = 0
        for button in self.operation_buttons:
            button.grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col > 2:
                col = 0
                row += 1

        self.calculate_button.grid(row=row + 1, column=0, columnspan=3, padx=10, pady=10)
        self.result_label.grid(row=row + 2, column=0, columnspan=3, padx=10, pady=10)

    def add_number(self, number):
        current_text = self.entry_num1.get()
        self.entry_num1.delete(0, tk.END)
        self.entry_num1.insert(0, current_text + str(number))

    def add_operation(self, operation):
        current_text = self.entry_num1.get()
        self.entry_num1.delete(0, tk.END)
        self.entry_num1.insert(0, current_text + operation)

    def calculate(self):
        try:
            expression = self.entry_num1.get()
            result = eval(expression)
            self.result_label.config(text=f"Result: {result}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
