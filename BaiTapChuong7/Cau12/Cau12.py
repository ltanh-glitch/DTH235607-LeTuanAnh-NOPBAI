from __future__ import annotations
import csv
import random
from pathlib import Path
from typing import Iterable, List

DATA_FILE = Path(__file__).with_name("random_matrix.csv")
DEFAULT_ROWS = 10
DEFAULT_COLS = 10
MAX_RANDOM_VALUE = 99


def generate_random_csv(rows: int = DEFAULT_ROWS, cols: int = DEFAULT_COLS) -> List[List[int]]:
    matrix: List[List[int]] = []
    with DATA_FILE.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, delimiter=";")
        for _ in range(rows):
            row = [random.randint(0, MAX_RANDOM_VALUE) for _ in range(cols)]
            writer.writerow(row)
            matrix.append(row)
    print(f"Tạo {rows} dòng x {cols} cột trong {DATA_FILE.name}.")
    return matrix


def read_and_sum_rows() -> List[int]:
    if not DATA_FILE.exists():
        raise FileNotFoundError(f"{DATA_FILE} không tồn tại. Chạy chức năng tạo file trước.")
    sums: List[int] = []
    with DATA_FILE.open(newline="", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter=";")
        for idx, row in enumerate(reader, start=1):
            numbers = [int(value) for value in row if value.strip()]
            row_sum = sum(numbers)
            sums.append(row_sum)
            print(f"Dòng {idx}: tổng = {row_sum}")
    return sums


def display_matrix(matrix: Iterable[Iterable[int]]) -> None:
    for row in matrix:
        print(";".join(str(value) for value in row))


def main() -> None:
    actions = {
        "1": "Tạo file CSV ngẫu nhiên",
        "2": "Đọc file và tính tổng từng dòng",
        "3": "Tạo rồi đọc",
        "0": "Thoát",
    }
    while True:
        print("\n--- Quản lý CSV Ma trận ---")
        for key, label in actions.items():
            print(f"{key}. {label}")
        choice = input("Chọn chức năng: ").strip()
        if choice == "1":
            matrix = generate_random_csv()
            print_matrix = input("Xem nhanh nội dung? (y/n): ").strip().lower()
            if print_matrix == "y":
                display_matrix(matrix)
        elif choice == "2":
            read_and_sum_rows()
        elif choice == "3":
            matrix = generate_random_csv()
            display_matrix(matrix)
            read_and_sum_rows()
        elif choice == "0":
            print("Kết thúc.")
            break
        else:
            print("Chọn đúng tùy chọn.")


if __name__ == "__main__":
    main()
