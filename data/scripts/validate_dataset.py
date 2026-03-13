import argparse
import json
import sys
from pathlib import Path

def validate_jsonl(path: Path) -> tuple[int, int, list[str]]:
    total = valid_turns = 0
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
            turns = row.get("turns")
            if not row.get("conversation_id") or not isinstance(turns, list) or not turns:
                errors.append(f"line {line_no}: missing conversation_id or non-empty turns")
                continue
            valid_turns += len(turns)
    return total, valid_turns, errors

def main() -> int:
    parser = argparse.ArgumentParser(description="Validate conversation JSONL datasets")
    parser.add_argument("input_file", type=Path)
    parser.add_argument("--strict", action="store_true", help="Exit non-zero if any errors exist")
    args = parser.parse_args()

    total, turns, issues = validate_jsonl(args.input_file)
    print(f"Checked {total} conversations ({turns} turns); {len(issues)} errors")
    for msg in issues[:25]:
        print(" -", msg)
    return 1 if (args.strict and issues) else 0

if __name__ == "__main__":
    sys.exit(main())
