import math
try:
    r=float(input("Mời bạn nhập bán kính hình tròn: "))
    cv=2*math.pi*r
    dt=r**2
    print("Chu vi hình tròn là: ", cv)
    print("Diện tích hình tròn là: ", dt)
except :
    print("Vui lòng nhập một số hợp lệ.")