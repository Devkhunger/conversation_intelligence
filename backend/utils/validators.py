from datetime import datetime
from typing import Any

REQUIRED_FIELDS = ("conversation_id", "turns")

def is_valid_iso_timestamp(value: str | None) -> bool:
    if not value or not isinstance(value, str):
        return False
    try:
        datetime.fromisoformat(value.replace("Z", "+00:00"))
        return True
    except ValueError:
        return False

def validate_conversation_payload(payload: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    for field in REQUIRED_FIELDS:
        if field not in payload or not payload[field]:
            errors.append(f"missing required field: {field}")
    turns = payload.get("turns")
    if not isinstance(turns, list):
        errors.append("turns must be a list")
        return errors
    for idx, turn in enumerate(turns):
        if not isinstance(turn, dict) or not str(turn.get("text", "")).strip():
            errors.append(f"turn[{idx}] missing text")
        if "timestamp" in turn and turn["timestamp"] is not None:
            if not is_valid_iso_timestamp(turn["timestamp"]):
                errors.append(f"turn[{idx}] invalid ISO-8601 timestamp")
    return errors
