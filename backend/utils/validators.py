from typing import Any

REQUIRED_FIELDS = ("conversation_id", "turns")

def validate_conversation_payload(payload: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    for field in REQUIRED_FIELDS:
        if field not in payload or not payload[field]:
            errors.append(f"missing required field: {field}")
    if isinstance(payload.get("turns"), list):
        for idx, turn in enumerate(payload["turns"]):
            if not isinstance(turn, dict) or not turn.get("text"):
                errors.append(f"turn[{idx}] missing text")
    return errors
