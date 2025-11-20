from __future__ import annotations
import json
from pathlib import Path
from typing import Dict, List

DATA_FILE = Path(__file__).with_name("students.json")

ClassEntry = Dict[str, object]
Student = Dict[str, object]


def load_data() -> Dict[str, ClassEntry]:
    if not DATA_FILE.exists():
        return {}
    with DATA_FILE.open(encoding="utf-8") as f:
        raw = json.load(f)
    return {code: {"name": entry["name"], "students": entry.get("students", [])} for code, entry in raw.items()}


def save_data(data: Dict[str, ClassEntry]) -> None:
    serializable = {}
    for code, entry in data.items():
        serializable[code] = {
            "name": entry["name"],
            "students": [{"code": s["code"], "name": s["name"], "year": s["year"]} for s in entry["students"]],
        }
    DATA_FILE.write_text(json.dumps(serializable, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Saved {DATA_FILE}")


def display(data: Dict[str, ClassEntry]) -> None:
    if not data:
        print("Chưa có lớp nào.")
        return
    for code, entry in data.items():
        print(f"Lớp {code} - {entry['name']}")
        if not entry["students"]:
            print("  (chưa có sinh viên)")
            continue
        for student in entry["students"]:
            print(f"  {student['code']} | {student['name']} | {student['year']}")


def prompt_nonempty(prompt: str) -> str:
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Không được để trống.")


def prompt_year(prompt: str) -> int:
    while True:
        value = input(prompt).strip()
        if not value:
            print("Nhập năm sinh.")
            continue
        if not value.isdigit():
            print("Phải là số nguyên.")
            continue
        return int(value)


def find_student(data: Dict[str, ClassEntry], student_code: str) -> tuple[ClassEntry, Student] | tuple[None, None]:
    for entry in data.values():
        for student in entry["students"]:
            if student["code"].lower() == student_code.lower():
                return entry, student
    return None, None


def search_students(data: Dict[str, ClassEntry]) -> None:
    keyword = input("Nhập mã hoặc tên sinh viên: ").strip().lower()
    if not keyword:
        print("Nhập gì đó để tìm.")
        return
    results: List[tuple[str, Student]] = []
    for class_code, entry in data.items():
        for student in entry["students"]:
            if keyword in student["code"].lower() or keyword in student["name"].lower():
                results.append((class_code, student))
    if not results:
        print("Không tìm thấy.")
        return
    for class_code, student in results:
        print(f"{student['code']} ({class_code}) - {student['name']} - {student['year']}")


def sort_students(data: Dict[str, ClassEntry]) -> None:
    for entry in data.values():
        entry["students"].sort(key=lambda s: s["name"].lower())
    print("Đã sắp xếp theo tên trong mỗi lớp.")


def main() -> None:
    data = load_data()
    menu = {
        "1": "Hiển thị danh sách lớp",
        "2": "Thêm lớp mới",
        "3": "Thêm sinh viên",
        "4": "Sửa lớp",
        "5": "Sửa sinh viên",
        "6": "Xóa lớp",
        "7": "Xóa sinh viên",
        "8": "Tìm sinh viên",
        "9": "Sắp xếp sinh viên",
        "S": "Lưu JSON",
        "L": "Tải lại JSON",
        "0": "Thoát",
    }
    while True:
        print("\n--- Quản lý sinh viên ---")
        for key, label in menu.items():
            print(f"{key}: {label}")
        choice = input("Chọn: ").strip().upper()
        if choice == "1":
            display(data)
        elif choice == "2":
            code = prompt_nonempty("Mã lớp: ")
            if code in data:
                print("Lớp đã tồn tại.")
                continue
            name = prompt_nonempty("Tên lớp: ")
            data[code] = {"name": name, "students": []}
            print("Đã thêm lớp.")
        elif choice == "3":
            if not data:
                print("Thêm lớp trước.")
                continue
            class_code = prompt_nonempty("Mã lớp của sinh viên: ")
            if class_code not in data:
                print("Lớp không tồn tại.")
                continue
            student_code = prompt_nonempty("Mã sinh viên: ")
            students = data[class_code]["students"]
            if any(s["code"].lower() == student_code.lower() for s in students):
                print("Mã sinh viên đã tồn tại trong lớp.")
                continue
            student = {
                "code": student_code,
                "name": prompt_nonempty("Tên sinh viên: "),
                "year": prompt_year("Năm sinh: "),
            }
            students.append(student)
            print("Đã thêm sinh viên.")
        elif choice == "4":
            code = prompt_nonempty("Mã lớp cần sửa: ")
            if code not in data:
                print("Lớp không tồn tại.")
                continue
            data[code]["name"] = prompt_nonempty("Tên mới: ")
            print("Cập nhật thành công.")
        elif choice == "5":
            student_code = prompt_nonempty("Mã sinh viên cần sửa: ")
            entry, student = find_student(data, student_code)
            if student is None:
                print("Không tìm thấy sinh viên.")
                continue
            student["name"] = prompt_nonempty("Tên mới: ")
            student["year"] = prompt_year("Năm sinh mới: ")
            print("Đã cập nhật.")
        elif choice == "6":
            code = prompt_nonempty("Mã lớp cần xóa: ")
            if code in data:
                del data[code]
                print("Đã xóa lớp.")
            else:
                print("Lớp không tồn tại.")
        elif choice == "7":
            student_code = prompt_nonempty("Mã sinh viên cần xóa: ")
            entry, student = find_student(data, student_code)
            if student is None:
                print("Không tìm thấy sinh viên.")
                continue
            entry["students"].remove(student)
            print("Đã xóa sinh viên.")
        elif choice == "8":
            search_students(data)
        elif choice == "9":
            sort_students(data)
        elif choice == "S":
            save_data(data)
        elif choice == "L":
            data = load_data()
            print("Đã tải lại dữ liệu từ JSON.")
        elif choice == "0":
            print("Kết thúc chương trình.")
            break
        else:
            print("Chọn chức năng hợp lệ.")


if __name__ == "__main__":
    main()
