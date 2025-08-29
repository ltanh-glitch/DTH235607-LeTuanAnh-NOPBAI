Câu 6: Trình bày ý nghĩa toán tử /, //, %, **, and, or, is.
1. Toán tử số học
  /: Chia lấy kết quả thực (luôn trả về số thực float).
    Ví dụ:
    print(7 / 2)   # 3.5
    print(8 / 4)   # 2.0

  //: Chia lấy phần nguyên (bỏ phần thập phân).
    Ví dụ:
    print(7 // 2)  # 3
    print(8 // 4)  # 2

  %: Chia lấy dư (modulo).
    Ví dụ:
    print(7 % 2)   # 1
    print(8 % 4)   # 0

  **: Lũy thừa.
    Ví dụ:
    print(2 ** 3)  # 8  (2 mũ 3)
    print(5 ** 2)  # 25

2. Toán tử logic
  and : Trả về True nếu cả 2 điều kiện đều đúng.
    Ví dụ:
    x = 5
    print(x > 2 and x < 10)   # True (5 lớn hơn 2 và nhỏ hơn 10)

  or : Trả về True nếu ít nhất 1 điều kiện đúng.
    Ví dụ:
    x = 5
    print(x < 2 or x < 10)    # True (vì 5 < 10 đúng)

3. Toán tử định danh (Identity operator)
  is : So sánh 2 biến có cùng tham chiếu (cùng vùng nhớ) hay không.
  Ví dụ:
  a = [1, 2, 3]
  b = a
  c = [1, 2, 3]
  print(a is b)  # True (b cùng tham chiếu với a)
  print(a is c)  # False (c có nội dung giống nhưng vùng nhớ khác a)
