from tkinter import *
from tkinter import messagebox

EXPECTED_USER = "admin"
EXPECTED_PASSWORD = "password"


def attempt_login() -> None:
    if user_var.get() == EXPECTED_USER and pass_var.get() == EXPECTED_PASSWORD:
        messagebox.showinfo("Đăng nhập", "Đăng nhập thành công!")
    else:
        messagebox.showerror("Đăng nhập", "Sai tên đăng nhập hoặc mật khẩu.")


def clear_fields() -> None:
    user_var.set("")
    pass_var.set("")


root = Tk()
root.title("Đăng nhập")
root.geometry("260x160")
root.resizable(False, False)

user_var = StringVar()
pass_var = StringVar()

Label(root, text="Đăng nhập", font=("Arial", 14, "bold"), pady=10).pack()
frame = Frame(root)
frame.pack(padx=10, pady=10)

Label(frame, text="Tên đăng nhập:").grid(row=0, column=0, sticky=W)
Entry(frame, textvariable=user_var, width=20).grid(row=0, column=1)
Label(frame, text="Mật khẩu:").grid(row=1, column=0, sticky=W)
Entry(frame, textvariable=pass_var, width=20, show="*").grid(row=1, column=1)

button_frame = Frame(root)
button_frame.pack(pady=(5, 0))
Button(button_frame, text="Đăng nhập", width=10, command=attempt_login).grid(row=0, column=0, padx=5)
Button(button_frame, text="Thoát", width=10, command=root.destroy).grid(row=0, column=1, padx=5)
Button(button_frame, text="Xóa", width=10, command=clear_fields).grid(row=1, column=0, columnspan=2, pady=(5, 0))

root.mainloop()
