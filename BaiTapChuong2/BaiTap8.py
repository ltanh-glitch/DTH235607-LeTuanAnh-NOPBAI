Câu 8: Trình bày các loại lỗi khi lập trình và cách bắt lỗi trong Python?
  1. Các loại lỗi thường gặp:
- Lỗi cú pháp (Syntax Error)
- Lỗi logic (Logic Error)
- Lỗi runtime (Runtime Error / Exception)
  2. Cách bắt lỗi trong Python:
- Python dùng cấu trúc try – except – finally để xử lý lỗi:
    a. Cơ bản với try – except
    try:
        x = int(input("Nhập số nguyên: "))
        print("Bạn nhập:", x)
    except ValueError:
        print("Lỗi: Bạn phải nhập số nguyên!")
  
    b. Dùng nhiều except cho nhiều loại lỗi
    try:
        a = int(input("Nhập a: "))
        b = int(input("Nhập b: "))
        print("Thương =", a / b)
    except ZeroDivisionError:
        print("Lỗi: Không thể chia cho 0!")
    except ValueError:
        print("Lỗi: Vui lòng nhập số hợp lệ!")
    
    c. Thêm else và finally
    else: chạy nếu không có lỗi.
    finally: luôn chạy dù có lỗi hay không, thường dùng để giải phóng tài nguyên.
    Ví dụ:
    try:
        num = int(input("Nhập số: "))
    except ValueError:
        print("Lỗi: nhập sai kiểu dữ liệu!")
    else:
        print("Bạn nhập số:", num)
    finally:
        print("Kết thúc chương trình.")
