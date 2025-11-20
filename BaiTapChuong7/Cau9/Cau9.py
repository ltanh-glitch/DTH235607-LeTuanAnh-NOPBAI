from __future__ import annotations
from pathlib import Path
from typing import Dict, List

DATA_FILE = Path(__file__).with_name("products.txt")

Category = Dict[str, object]
Product = Dict[str, object]


def load_data() -> Dict[str, Category]:
    categories: Dict[str, Category] = {}
    if not DATA_FILE.exists():
        return categories
    for line in DATA_FILE.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split("|")
        if parts[0] == "CAT" and len(parts) >= 3:
            code = parts[1]
            name = parts[2]
            categories.setdefault(code, {"name": name, "products": []})
        elif parts[0] == "PRO" and len(parts) >= 5:
            cat_code, prod_code, prod_name, price_str = parts[1], parts[2], parts[3], parts[4]
            entry = categories.setdefault(cat_code, {"name": "<unknown>", "products": []})
            entry["products"].append({
                "code": prod_code,
                "name": prod_name,
                "price": float(price_str),
            })
    return categories


def save_data(categories: Dict[str, Category]) -> None:
    lines: List[str] = []
    for cat_code, cat in categories.items():
        lines.append(f"CAT|{cat_code}|{cat['name']}")
        for prod in cat["products"]:
            lines.append(
                f"PRO|{cat_code}|{prod['code']}|{prod['name']}|{prod['price']}"
            )
    DATA_FILE.write_text("\n".join(lines), encoding="utf-8")
    print(f"Saved {DATA_FILE}" )


def display(categories: Dict[str, Category]) -> None:
    if not categories:
        print("Chưa có danh mục nào.")
        return
    for cat_code, cat in categories.items():
        print(f"Danh mục {cat_code} - {cat['name']}")
        products = cat["products"]
        if not products:
            print("  (chưa có sản phẩm)")
            continue
        for prod in products:
            print(f"  {prod['code']} | {prod['name']} | {prod['price']:.0f} VND")


def prompt_nonempty(text: str) -> str:
    while True:
        value = input(text).strip()
        if value:
            return value
        print("Vui lòng nhập giá trị không rỗng.")


def prompt_price(text: str) -> float:
    while True:
        value = input(text).strip()
        if not value:
            print("Yêu cầu nhập số.")
            continue
        try:
            return float(value)
        except ValueError:
            print("Số không hợp lệ. Nhập lại.")


def find_product(categories: Dict[str, Category], prod_code: str) -> tuple[Category, Product] | tuple[None, None]:
    for cat in categories.values():
        for prod in cat["products"]:
            if prod["code"].lower() == prod_code.lower():
                return cat, prod
    return None, None


def search(categories: Dict[str, Category]) -> None:
    query = input("Nhập mã hoặc tên sản phẩm cần tìm: ").strip().lower()
    if not query:
        print("Không tìm kiếm gì được.")
        return
    found = []
    for cat_code, cat in categories.items():
        for prod in cat["products"]:
            if query in prod["code"].lower() or query in prod["name"].lower():
                found.append((cat_code, prod))
    if not found:
        print("Không có sản phẩm phù hợp.")
        return
    for cat_code, prod in found:
        print(f"{prod['code']} ({cat_code}) - {prod['name']} - {prod['price']:.0f}")


def sort_products(categories: Dict[str, Category]) -> None:
    for cat in categories.values():
        cat["products"].sort(key=lambda p: p["price"])
    print("Đã sắp xếp các sản phẩm theo giá tăng dần từng danh mục.")


def main() -> None:
    categories = load_data()
    actions = {
        "1": "Hiển thị danh sách",
        "2": "Thêm danh mục mới",
        "3": "Thêm sản phẩm",
        "4": "Sửa danh mục",
        "5": "Sửa sản phẩm",
        "6": "Xóa danh mục",
        "7": "Xóa sản phẩm",
        "8": "Tìm kiếm sản phẩm",
        "9": "Sắp xếp sản phẩm",
        "S": "Lưu file",
        "L": "Tải lại file",
        "0": "Thoát",
    }
    while True:
        print("\n--- Quản lý sản phẩm ---")
        for key, label in actions.items():
            print(f"{key}: {label}")
        choice = input("Chọn chức năng: ").strip().upper()
        if choice == "1":
            display(categories)
        elif choice == "2":
            code = prompt_nonempty("Mã danh mục: ")
            name = prompt_nonempty("Tên danh mục: ")
            if code in categories:
                print("Danh mục tồn tại.")
            else:
                categories[code] = {"name": name, "products": []}
                print("Đã thêm danh mục.")
        elif choice == "3":
            if not categories:
                print("Chưa có danh mục. Thêm danh mục trước.")
                continue
            cat_code = prompt_nonempty("Mã danh mục sản phẩm: ")
            if cat_code not in categories:
                print("Danh mục không tồn tại.")
                continue
            prod_code = prompt_nonempty("Mã sản phẩm: ")
            cat = categories[cat_code]
            if any(p["code"].lower() == prod_code.lower() for p in cat["products"]):
                print("Mã sản phẩm đã tồn tại trong danh mục.")
                continue
            prod = {
                "code": prod_code,
                "name": prompt_nonempty("Tên sản phẩm: "),
                "price": prompt_price("Đơn giá: "),
            }
            cat["products"].append(prod)
            print("Đã thêm sản phẩm.")
        elif choice == "4":
            code = prompt_nonempty("Mã danh mục cần sửa: ")
            if code not in categories:
                print("Danh mục không tồn tại.")
                continue
            categories[code]["name"] = prompt_nonempty("Tên mới: ")
            print("Đã cập nhật danh mục.")
        elif choice == "5":
            prod_code = prompt_nonempty("Mã sản phẩm cần sửa: ")
            cat, prod = find_product(categories, prod_code)
            if prod is None:
                print("Không tìm thấy sản phẩm.")
                continue
            prod["name"] = prompt_nonempty("Tên mới: ")
            prod["price"] = prompt_price("Đơn giá mới: ")
            print("Đã cập nhật sản phẩm.")
        elif choice == "6":
            code = prompt_nonempty("Mã danh mục cần xóa: ")
            if code in categories:
                del categories[code]
                print("Đã xóa danh mục.")
            else:
                print("Danh mục không tồn tại.")
        elif choice == "7":
            prod_code = prompt_nonempty("Mã sản phẩm cần xóa: ")
            cat, prod = find_product(categories, prod_code)
            if prod is None:
                print("Không tìm thấy sản phẩm.")
                continue
            cat["products"].remove(prod)
            print("Đã xóa sản phẩm.")
        elif choice == "8":
            search(categories)
        elif choice == "9":
            sort_products(categories)
        elif choice == "S":
            save_data(categories)
        elif choice == "L":
            categories = load_data()
            print("Đã tải lại dữ liệu từ file.")
        elif choice == "0":
            print("Kết thúc chương trình.")
            break
        else:
            print("Chọn chức năng hợp lệ.")


if __name__ == "__main__":
    main()
