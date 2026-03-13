import json
import sys
from pathlib import Path

def validate_file(path: Path) -> int:
    data = json.loads(path.read_text(encoding="utf-8"))
    invalid = 0
    for row in data:
        if not row.get("conversation_id") or not row.get("turns"):
            invalid += 1
    return invalid

if __name__ == "__main__":
    target = Path(sys.argv[1])
    bad = validate_file(target)
    print(f"Invalid records: {bad}")
