
import csv
from etl import transform_data


def test_transform_data(tmp_path):
    input_file = tmp_path / "input.csv"
    output_file = tmp_path / "output.csv"

    input_file.write_text(
        "name,amount\nAlice,100\n,300\nBob,200\n",
        encoding="utf-8",
    )

    count = transform_data(input_file, output_file)

    assert count == 2

    with output_file.open(encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    assert rows == [
        {"name": "Alice", "amount": "100.0"},
        {"name": "Bob", "amount": "200.0"},
    ]
