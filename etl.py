
import csv
from pathlib import Path


def transform_data(input_file, output_file):
    input_path = Path(input_file)
    output_path = Path(output_file)

    with input_path.open("r", newline="", encoding="utf-8") as source:
        reader = csv.DictReader(source)
        rows = list(reader)

    cleaned_rows = [
        {
            "name": row["name"].strip(),
            "amount": float(row["amount"]),
        }
        for row in rows
        if row.get("name", "").strip() and row.get("amount", "").strip()
    ]

    with output_path.open("w", newline="", encoding="utf-8") as target:
        writer = csv.DictWriter(
            target, fieldnames=["name", "amount"]
        )
        writer.writeheader()
        writer.writerows(cleaned_rows)

    return len(cleaned_rows)
