import re
from typing import Any

SMART_QUOTES = str.maketrans({
    "\u2018": "'", "\u2019": "'", "\u201c": '"', "\u201d": '"', "\u00a0": " "
})

SPEAKER_ALIASES = {
    "rep": "agent",
    "support": "agent",
    "client": "customer",
    "user": "customer",
}

def normalize_speaker(raw: str | None) -> str:
    label = (raw or "unknown").strip().lower()
    return SPEAKER_ALIASES.get(label, label)

def clean_text(text: str | None) -> str:
    if not text:
        return ""
    normalized = text.translate(SMART_QUOTES)
    return re.sub(r"\s+", " ", normalized).strip()

def clean_turns(turns: list[dict[str, Any]]) -> list[dict[str, Any]]:
    cleaned = []
    for t in turns:
        body = clean_text(t.get("text"))
        if not body:
            continue
        cleaned.append({
            "speaker": normalize_speaker(t.get("speaker")),
            "text": body,
            "timestamp": t.get("timestamp"),
        })
    return cleaned
