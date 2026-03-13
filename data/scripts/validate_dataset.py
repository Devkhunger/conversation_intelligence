import json
import sys
from pathlib import Path

def validate_jsonl(path: Path) -> tuple[int, list[str]]:
    total = 0
    errors: list[str] = []
    with path.open("r", encoding="utf-8") as fh:
        for line_no, raw in enumerate(fh, start=1):
            raw = raw.strip()
            if not raw:
                continue
            total += 1
            try:
                row = json.loads(raw)
            except json.JSONDecodeError as exc:
                errors.append(f"line {line_no}: malformed JSON ({exc.msg})")
                continue
            if not row.get("conversation_id") or not isinstance(row.get("turns"), list):
                errors.append(f"line {line_no}: missing conversation_id or turns")
    return total, errors

if __name__ == "__main__":
    target = Path(sys.argv[1])
    total, issues = validate_jsonl(target)
    print(f"Checked {total} records; {len(issues)} issues found")
    for msg in issues[:20]:
        print(" -", msg)
