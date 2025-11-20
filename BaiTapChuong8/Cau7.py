from tkinter import *
import datetime

CHU_KY_CAN = ["Canh", "Tân", "Nhâm", "Quý", "Giáp", "Ất", "Bính", "Đinh", "Mậu", "Kỷ"]
CHU_KY_CHI = ["Thân", "Dậu", "Tuất", "Hợi", "Tý", "Sửu", "Dần", "Mão", "Thìn", "Tỵ", "Ngọ", "Mùi"]


def convert_year() -> None:
    year_str = entry_year.get().strip()
    if not year_str.isdigit():
        label_result.config(text="Nhập số nguyên dương", fg="red")
        return
    year = int(year_str)
    idx_can = (year - 1984 + 4) % 10
    idx_chi = (year - 1984 + 4) % 12
    label_result.config(text=f"{CHU_KY_CAN[idx_can]} {CHU_KY_CHI[idx_chi]}", fg="blue")


def clear_input() -> None:
    entry_year.delete(0, END)
    label_result.config(text="", fg="blue")


root = Tk()
root.title("Chuyển năm dương sang âm")
root.geometry("360x200")
root.configure(bg="#f3df00")
root.resizable(False, False)

frame = Frame(root, bg="#f3df00", padx=15, pady=15)
frame.pack(fill=BOTH, expand=True)

Label(frame, text="Nhập năm dương:", font=("Arial", 12), bg="#f3df00").grid(row=0, column=0, sticky=W)
entry_year = Entry(frame, width=10, font=("Arial", 14), justify=CENTER)
entry_year.grid(row=0, column=1, padx=10, pady=5)
entry_year.insert(0, str(datetime.datetime.now().year))

button = Button(frame, text="Chuyển", font=("Helvetica", 12, "bold"), bg="#1662d4", fg="white", command=convert_year)
button.grid(row=0, column=2, padx=5)

Label(frame, text="Năm âm:", font=("Arial", 12), bg="#f3df00").grid(row=1, column=0, pady=10, sticky=W)
label_result = Label(frame, text="", font=("Arial", 14, "bold"), bg="#f3df00", fg="blue")
label_result.grid(row=1, column=1, columnspan=2)

Button(frame, text="Xóa", width=10, command=clear_input).grid(row=2, column=0, columnspan=3, pady=10)
root.mainloop()
