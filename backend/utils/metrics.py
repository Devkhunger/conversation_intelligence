from collections import defaultdict

def compute_talk_ratio(turns: list[dict]) -> dict[str, float]:
    word_counts: dict[str, int] = defaultdict(int)
    total = 0
    for turn in turns:
        words = len((turn.get("text") or "").split())
        speaker = turn.get("speaker") or "unknown"
        word_counts[speaker] += words
        total += words
    if total == 0:
        return {}
    return {s: round(c / total, 4) for s, c in word_counts.items()}

def average_turn_words(turns: list[dict]) -> float:
    if not turns:
        return 0.0
    words = [len((t.get("text") or "").split()) for t in turns]
    return round(sum(words) / len(words), 2)
