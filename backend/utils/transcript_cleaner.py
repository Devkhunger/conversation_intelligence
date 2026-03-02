import re

SMART_QUOTES = str.maketrans({
    "\u2018": "'", "\u2019": "'", "\u201c": '"', "\u201d": '"', "\u00a0": " "
})

def clean_text(text: str) -> str:
    if not text:
        return ""
    normalized = text.translate(SMART_QUOTES)
    return re.sub(r"\s+", " ", normalized).strip()

def clean_turns(turns: list[dict]) -> list[dict]:
    cleaned = []
    for t in turns:
        body = clean_text(t.get("text") or "")
        if not body:
            continue
        cleaned.append({
            "speaker": (t.get("speaker") or "unknown").strip(),
            "text": body,
            "timestamp": t.get("timestamp"),
        })
    return cleaned
