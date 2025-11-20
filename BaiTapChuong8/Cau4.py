from tkinter import *


def append_char(char: str) -> None:
    current = display.get()
    display.set(current + char)


def clear_display() -> None:
    display.set("")


def calculate() -> None:
    try:
        result = eval(display.get())
    except Exception:
        display.set("Error")
    else:
        display.set(str(result))


root = Tk()
root.title("Máy tính bỏ túi")
root.resizable(False, False)

display = StringVar()
Entry(root, textvariable=display, justify=RIGHT, bd=5, font=("Arial", 18)).grid(row=0, column=0, columnspan=4, ipady=10)

buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
]

for (text, row, col) in buttons:
    action = calculate if text == "=" else (lambda t=text: append_char(t))
    Button(root, text=text, width=5, height=2, command=action).grid(row=row, column=col, padx=2, pady=2)

Button(root, text="Clr", width=23, command=clear_display).grid(row=5, column=0, columnspan=4, pady=(5, 0))

root.mainloop()
