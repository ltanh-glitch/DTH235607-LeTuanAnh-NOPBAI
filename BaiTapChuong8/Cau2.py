from tkinter import * 
 
from math import sqrt 
def giaiAction(): 
    a=float(stringHSA.get()) 
    b = float(stringHSB.get()) 
    c = float(stringHSC.get()) 
    if a==0:#bx+c=0 
        if b==0 and c==0: 
            stringKQ.set("Vô số nghiệm") 
        elif b==0 and c!=0: 
            stringKQ.set("Vô nghiệm") 
        else: 
            x=-c/b 
            stringKQ.set("x="+str(x)) 
    else: 
        delta=b**2-4*a*c 
        if delta<0: 
            stringKQ.set("Vô nghiệm") 
        elif delta==0: 
            stringKQ.set("No kép x1=x2="+str((-b/(2*a)))) 
        else: 
            x1=(-b-sqrt(delta))/(2*a) 
            x2 = (-b + sqrt(delta)) / (2 * a) 
            stringKQ.set("x1="+str(x1)+";x2="+str(x2)) 
def tiepAction(): 
    stringHSA.set("") 
    stringHSB.set("") 
    stringHSC.set("") 
    stringKQ.set("") 
root=Tk() 
stringHSA=StringVar() 
stringHSB=StringVar() 
stringHSC=StringVar() 
stringKQ=StringVar() 
root.title("PTB2") 
root.minsize(height=150,width=250) 
 
Label(root,text="Phương Trình bậc 2",fg="red",font=("tahoma",16)).grid(row=0,column=0,columnspan=2) 
Label(root,text="Hệ số a:").grid(row=1,column=0) 
Entry(root,width=30,textvariable=stringHSA).grid(row=1,column=1) 
Label(root,text="Hệ số b:").grid(row=2,column=0) 
Entry(root,width=30,textvariable=stringHSB).grid(row=2,column=1) 
Label(root,text="Hệ số c:").grid(row=3,column=0) 
Entry(root,width=30,textvariable=stringHSC).grid(row=3,column=1) 
 
frameButton=Frame() 
Button(frameButton,text="Giải",command=giaiAction).pack(side=LEFT) 
Button(frameButton,text="Tiếp", command=tiepAction).pack(side=LEFT) 
Button(frameButton,text="Thoát",command=root.quit).pack(side=LEFT) 
 
frameButton.grid(row=4,columnspan=2) 
 
Label(root,text="Kết quả:").grid(row=5,column=0) 
Entry(root,width=30,textvariable=stringKQ).grid(row=5,column=1) 
 
root.mainloop()