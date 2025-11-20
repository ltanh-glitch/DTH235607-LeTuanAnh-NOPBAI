import csv
from pathlib import Path

# CSV file should sit alongside this script
DATA_FILE = Path(__file__).with_name("datacsv.csv")

if not DATA_FILE.exists():
    raise FileNotFoundError(DATA_FILE)

with DATA_FILE.open(newline="", encoding="utf-8") as csv_file:
    reader = csv.reader(csv_file, delimiter=";", quoting=csv.QUOTE_NONE)
    for row in reader:
        if len(row) < 2:
            continue
        print(row[0], "\t", row[1])
