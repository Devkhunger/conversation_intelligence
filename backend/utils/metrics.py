from collections import defaultdict

def compute_talk_ratio(turns: list[dict]) -> dict[str, float]:
    word_counts: dict[str, int] = defaultdict(int)
    total = 0
    for turn in turns:
        words = len(turn.get("text", "").split())
        speaker = turn.get("speaker", "unknown")
        word_counts[speaker] += words
        total += words
    return {s: round(c / total, 4) for s, c in word_counts.items()}

def average_turn_words(turns: list[dict]) -> float:
    words = [len(t.get("text", "").split()) for t in turns]
    return round(sum(words) / len(words), 2)
