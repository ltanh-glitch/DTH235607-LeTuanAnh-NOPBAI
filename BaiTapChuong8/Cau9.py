from tkinter import *

BACKGROUND = "#FFE500"
FONT_LABEL = ("Arial", 12)
FONT_ENTRY = ("Arial", 14, "bold")

root = Tk()
root.title("Tính BMI")
root.configure(bg=BACKGROUND)
root.resizable(False, False)
root.geometry("360x320")

frame = Frame(root, bg=BACKGROUND, padx=20, pady=20)
frame.pack(fill=BOTH, expand=True)

Label(frame, text="Nhập chiều cao (m):", bg=BACKGROUND, font=FONT_LABEL).grid(row=0, column=0, sticky=W, pady=5)
entry_height = Entry(frame, width=18, font=FONT_ENTRY, justify=CENTER)
entry_height.grid(row=0, column=1, pady=5)

Label(frame, text="Nhập cân nặng (kg):", bg=BACKGROUND, font=FONT_LABEL).grid(row=1, column=0, sticky=W, pady=5)
entry_weight = Entry(frame, width=18, font=FONT_ENTRY, justify=CENTER)
entry_weight.grid(row=1, column=1, pady=5)

label_bmi = Label(frame, text="BMI của bạn:", bg=BACKGROUND, font=FONT_LABEL)
label_bmi.grid(row=2, column=0, sticky=W, pady=5)
bmi_var = StringVar(value="X")
entry_bmi = Entry(frame, font=FONT_ENTRY, width=18, justify=CENTER, textvariable=bmi_var, state="readonly")
entry_bmi.grid(row=2, column=1, pady=5)

label_status = Label(frame, text="Tình trạng của bạn:", bg=BACKGROUND, font=FONT_LABEL)
label_status.grid(row=3, column=0, sticky=W, pady=5)
status_var = StringVar(value="X")
entry_status = Entry(frame, font=FONT_ENTRY, width=18, justify=CENTER, textvariable=status_var, state="readonly")
entry_status.grid(row=3, column=1, pady=5)

label_risk = Label(frame, text="Nguy cơ phát triển bệnh:", bg=BACKGROUND, font=FONT_LABEL)
label_risk.grid(row=4, column=0, sticky=W, pady=5)
risk_var = StringVar(value="X")
entry_risk = Entry(frame, font=FONT_ENTRY, width=18, justify=CENTER, textvariable=risk_var, state="readonly")
entry_risk.grid(row=4, column=1, pady=5)


BMI_RULES = [
    (18.5, "Gầy", "Thấp"),
    (24.9, "Bình thường", "Bình thường"),
    (29.9, "Mập", "Hơi cao"),
    (float("inf"), "Béo phì", "Cao"),
]


def calculate_bmi() -> None:
    try:
        height = float(entry_height.get())
        weight = float(entry_weight.get())
        if height <= 0 or weight <= 0:
            raise ValueError
    except ValueError:
        bmi_var.set("Không hợp lệ")
        status_var.set("")
        risk_var.set("")
        return
    bmi = weight / (height * height)
    bmi_var.set(f"{bmi:.2f}")
    for limit, status, risk in BMI_RULES:
        if bmi <= limit:
            status_var.set(status)
            risk_var.set(risk)
            break


Button(frame, text="Tính BMI", font=("Arial", 12), bg="#146EE2", fg="white", width=20, command=calculate_bmi).grid(row=5, column=0, columnspan=2, pady=15)
Button(frame, text="Thoát", font=("Arial", 10), bg="#777", fg="white", width=28, command=root.destroy).grid(row=6, column=0, columnspan=2)

root.mainloop()
