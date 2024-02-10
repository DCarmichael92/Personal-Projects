import tkinter as tk
import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero!"
    else:
        return x / y

def exponentiate(x, y):
    return x ** y

def square_root(x):
    if x < 0:
        return "Cannot compute square root of a negative number!"
    else:
        return math.sqrt(x)

def modulus(x, y):
    if y == 0:
        return "Cannot compute modulus with divisor zero!"
    else:
        return x % y

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, str(current) + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    ("1", 1, 0), ("2", 1, 1), ("3", 1, 2), ("4", 2, 0),
    ("5", 2, 1), ("6", 2, 2), ("7", 3, 0), ("8", 3, 1),
    ("9", 3, 2), ("0", 4, 1), ("+", 1, 3), ("-", 2, 3),
    ("*", 3, 3), ("/", 4, 3), ("=", 4, 2), ("C", 4, 0)
]

for (text, row, column) in buttons:
    if text == "=":
        button = tk.Button(root, text=text, padx=30, pady=20, command=button_equal)
    elif text == "C":
        button = tk.Button(root, text=text, padx=30, pady=20, command=button_clear)
    else:
        button = tk.Button(root, text=text, padx=30, pady=20, command=lambda text=text: button_click(text))
    button.grid(row=row, column=column, padx=5, pady=5)

root.mainloop()
