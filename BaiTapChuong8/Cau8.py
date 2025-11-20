from tkinter import *

root = Tk()
root.title("Chuyển độ F sang C")
root.geometry("460x220")
root.configure(bg="#f9eb2f")
root.resizable(False, False)

frame = Frame(root, bg="#f9eb2f", padx=20, pady=20)
frame.pack(fill=BOTH, expand=True)

Label(frame, text="Nhập độ F", font=("Arial", 14), bg="#f9eb2f").grid(row=0, column=0, sticky=W)
f_entry = Entry(frame, font=("Arial", 16), width=10, justify=CENTER)
f_entry.grid(row=0, column=1, padx=10, pady=5)

result_var = StringVar(value="Độ C ở đây")
Label(frame, text="Độ C", font=("Arial", 14), bg="#f9eb2f").grid(row=1, column=0, sticky=W)
Label(frame, textvariable=result_var, font=("Arial", 16, "bold"), bg="#f9eb2f", fg="blue").grid(row=1, column=1)


def convert():
    try:
        f_value = float(f_entry.get())
    except ValueError:
        result_var.set("Giá trị không hợp lệ")
    else:
        c = (f_value - 32) * 5 / 9
        result_var.set(f"{c:.2f} °C")

Button(frame, text="Chuyển", font=("Arial", 12, "bold"), width=12, bg="#146ed4", fg="white", command=convert).grid(row=0, column=2, rowspan=2, padx=10)

root.mainloop()
