from __future__ import annotations
from pathlib import Path
from typing import Dict, List
import xml.etree.ElementTree as ET

GROUP_FILE = Path(__file__).with_name("nhomthietbi.xml")
DEVICE_FILE = Path(__file__).with_name("ThietBi.xml")

Group = Dict[str, str]
Device = Dict[str, str]


def load_groups() -> Dict[str, Group]:
    if not GROUP_FILE.exists():
        raise FileNotFoundError(f"{GROUP_FILE.name} missing")
    tree = ET.parse(GROUP_FILE)
    root = tree.getroot()
    groups: Dict[str, Group] = {}
    for elem in root.findall("nhom"):
        code = elem.findtext("ma", "").strip()
        name = elem.findtext("ten", "").strip()
        if not code:
            continue
        groups[code] = {"code": code, "name": name}
    return groups


def load_devices() -> List[Device]:
    if not DEVICE_FILE.exists():
        raise FileNotFoundError(f"{DEVICE_FILE.name} missing")
    tree = ET.parse(DEVICE_FILE)
    root = tree.getroot()
    devices: List[Device] = []
    for elem in root.findall("thietbi"):
        code = elem.findtext("ma", "").strip()
        name = elem.findtext("ten", "").strip()
        group_code = elem.get("manhom", "").strip()
        if not code or not group_code:
            continue
        devices.append({"code": code, "name": name, "group": group_code})
    return devices


def display_groups(groups: Dict[str, Group]) -> None:
    print("Danh sách nhóm:")
    for group in groups.values():
        print(f"  {group['code']} - {group['name']}")


def display_devices(devices: List[Device], groups: Dict[str, Group]) -> None:
    print("Toàn bộ thiết bị:")
    for device in devices:
        group_name = groups.get(device["group"], {}).get("name", "<chưa xác định>")
        print(f"  {device['code']} | {device['name']} | nhóm {device['group']} ({group_name})")


def devices_by_group(devices: List[Device], group_code: str) -> List[Device]:
    return [d for d in devices if d["group"].lower() == group_code.lower()]


def top_group(groups: Dict[str, Group], devices: List[Device]) -> Group | None:
    count: Dict[str, int] = {code: 0 for code in groups}
    for device in devices:
        if device["group"] in count:
            count[device["group"]] += 1
    if not count:
        return None
    best = max(count.items(), key=lambda item: (item[1], item[0]))
    group = groups.get(best[0])
    if group:
        print(f"Nhóm nhiều thiết bị nhất: {group['code']} ({group['name']}) với {best[1]} thiết bị")
    return group


def main() -> None:
    groups = load_groups()
    devices = load_devices()
    while True:
        print("\n--- Quản lý thiết bị ---")
        print("1. Hiển thị danh sách nhóm")
        print("2. Hiển thị toàn bộ thiết bị")
        print("3. Lọc theo nhóm")
        print("4. Nhóm có nhiều thiết bị nhất")
        print("0. Thoát")
        choice = input("Chọn: ").strip()
        match choice:
            case "1":
                display_groups(groups)
            case "2":
                display_devices(devices, groups)
            case "3":
                code = input("Mã nhóm muốn lọc: ").strip()
                filtered = devices_by_group(devices, code)
                if not filtered:
                    print("Không tìm thấy thiết bị nào trong nhóm đó.")
                else:
                    print(f"Thiết bị nhóm {code}:")
                    for dev in filtered:
                        print(f"  {dev['code']} | {dev['name']}")
            case "4":
                top_group(groups, devices)
            case "0":
                print("Kết thúc.")
                break
            case _:
                print("Chọn hợp lệ.")


if __name__ == "__main__":
    main()
