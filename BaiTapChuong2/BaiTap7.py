Câu 7: Trình bày một số cách nhập dữ liệu từ bàn phím?

1. Nhập chuỗi (string)
name = input("Nhập tên của bạn: ")
print("Xin chào,", name)

2. Nhập số nguyên (int)
age = int(input("Nhập tuổi của bạn: "))
print("Năm sau bạn sẽ:", age + 1)

3. Nhập số thực (float)
height = float(input("Nhập chiều cao (m): "))
print("Chiều cao bạn là:", height, "m")

4. Nhập nhiều giá trị trên 1 dòng (sử dụng split())
a, b = input("Nhập 2 số cách nhau bởi khoảng trắng: ").split()
print("Bạn đã nhập:", a, b)
=> Lưu ý: mặc định a, b sẽ là chuỗi. Nếu muốn số thì ép kiểu:
a, b = map(int, input("Nhập 2 số nguyên: ").split())
print("Tổng =", a + b)

5. Nhập danh sách nhiều phần tử
num = list(map(int, input("Nhập các số nguyên cách nhau bởi khoảng trắng: ").split()))
print("Danh sách số:", num)
