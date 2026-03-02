import re

def clean_text(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()

def clean_turns(turns: list[dict]) -> list[dict]:
    cleaned = []
    for t in turns:
        cleaned.append({
            "speaker": t.get("speaker", "unknown"),
            "text": clean_text(t.get("text", "")),
        })
    return cleaned
