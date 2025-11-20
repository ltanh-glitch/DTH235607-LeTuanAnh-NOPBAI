from pathlib import Path
import re
from typing import Iterable, List


def parse_numbers(line: str) -> List[int]:
    tokens = [token for token in re.split(r"[\s,]+", line.strip()) if token]
    return [int(token) for token in tokens]


def read_number_lines(path: Path) -> List[List[int]]:
    lines: List[List[int]] = []
    with path.open("r", encoding="utf-8") as stream:
        for raw_line in stream:
            stripped = raw_line.strip()
            if not stripped:
                continue
            lines.append(parse_numbers(stripped))
    return lines


def print_line_lists(number_lines: Iterable[List[int]]) -> None:
    for idx, numbers in enumerate(number_lines, start=1):
        print(f"Dòng {idx}: {numbers}")


def print_negative_values(number_lines: Iterable[List[int]]) -> None:
    for idx, numbers in enumerate(number_lines, start=1):
        negatives = [num for num in numbers if num < 0]
        label = negatives if negatives else "Không có"
        print(f"Dòng {idx} số âm: {label}")


def main() -> None:
    data_file = Path(__file__).with_name("csdl_so.txt")
    if not data_file.exists():
        raise FileNotFoundError(f"Thiếu tệp dữ liệu: {data_file}")
    number_lines = read_number_lines(data_file)
    print_line_lists(number_lines)
    print_negative_values(number_lines)


if __name__ == "__main__":
    main()