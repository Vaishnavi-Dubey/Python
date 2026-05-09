"""
Python File Handling and Serialization.
Covers text/binary I/O, CSV, and JSON handling using pathlib and context managers.
"""

import json
import csv
from pathlib import Path
from typing import List, Dict, Any

def write_text_file(path: Path, content: str) -> None:
    """Writes a string to a text file using pathlib."""
    path.write_text(content, encoding='utf-8')

def read_text_file(path: Path) -> str:
    """Reads a string from a text file."""
    return path.read_text(encoding='utf-8')

def save_json_data(path: Path, data: Any) -> None:
    """Saves data to a JSON file."""
    with path.open('w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

def load_json_data(path: Path) -> Any:
    """Loads data from a JSON file."""
    with path.open('r', encoding='utf-8') as f:
        return json.load(f)

def write_csv_data(path: Path, data: List[List[str]]) -> None:
    """Writes data to a CSV file."""
    with path.open('w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(data)

def read_csv_data(path: Path) -> List[List[str]]:
    """Reads data from a CSV file."""
    with path.open('r', encoding='utf-8') as f:
        reader = csv.reader(f)
        return list(reader)

if __name__ == "__main__":
    # Setup temporary paths
    temp_dir = Path("temp_files")
    temp_dir.mkdir(exist_ok=True)
    
    text_file = temp_dir / "sample.txt"
    json_file = temp_dir / "data.json"
    csv_file = temp_dir / "data.csv"

    # Text operations
    write_text_file(text_file, "Hello Python File Handling!")
    print(f"Read Text: {read_text_file(text_file)}")

    # JSON operations
    user_data = {"id": 1, "name": "Vaishnavi", "role": "Developer"}
    save_json_data(json_file, user_data)
    print(f"Loaded JSON: {load_json_data(json_file)}")

    # CSV operations
    rows = [["ID", "Name"], ["101", "Alice"], ["102", "Bob"]]
    write_csv_data(csv_file, rows)
    print(f"Read CSV: {read_csv_data(csv_file)}")

    # Cleanup (Optional)
    # text_file.unlink(); json_file.unlink(); csv_file.unlink(); temp_dir.rmdir()
