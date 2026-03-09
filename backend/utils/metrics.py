from collections import Counter, defaultdict

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

def speaker_turn_counts(turns: list[dict]) -> dict[str, int]:
    return dict(Counter(t.get("speaker") or "unknown" for t in turns))

def longest_monologue_words(turns: list[dict]) -> int:
    best = current = 0
    prev_speaker = None
    for turn in turns:
        speaker = turn.get("speaker") or "unknown"
        words = len((turn.get("text") or "").split())
        current = current + words if speaker == prev_speaker else words
        prev_speaker = speaker
        best = max(best, current)
    return best
