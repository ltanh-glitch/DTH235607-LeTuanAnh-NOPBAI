from tkinter import *

RELIEFS = ["raised", "sunken", "flat", "ridge", "groove", "solid"]

root = Tk()
root.title("Button Styles")
root.geometry("660x240")
root.resizable(False, False)

frame = Frame(root, padx=12, pady=12)
frame.pack(fill=BOTH, expand=True)

for row, borderwidth in enumerate(range(5), start=0):
    Label(frame, text=f"borderwidth = {borderwidth}", width=14, anchor=W).grid(row=row, column=0, sticky=W, pady=2)
    for col, relief in enumerate(RELIEFS, start=1):
        Button(
            frame,
            text=relief,
            relief=relief,
            borderwidth=borderwidth,
            width=10,
            height=1,
        ).grid(row=row, column=col, padx=4, pady=2)

for i in range(len(RELIEFS) + 1):
    frame.grid_columnconfigure(i, weight=1)

root.mainloop()
