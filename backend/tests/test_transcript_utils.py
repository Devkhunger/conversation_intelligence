import unittest
from backend.utils.transcript_cleaner import clean_turns, normalize_speaker
from backend.utils.validators import validate_conversation_payload

class TestTranscriptUtils(unittest.TestCase):
    def test_clean_turns_drops_empty_and_normalizes_speaker(self):
        raw = [
            {"speaker": "Rep", "text": "  Hello\u2019s   world  "},
            {"speaker": "User", "text": "   "},
        ]
        result = clean_turns(raw)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["speaker"], "agent")
        self.assertEqual(result[0]["text"], "Hello's world")
        self.assertEqual(normalize_speaker("Client"), "customer")

    def test_validator_catches_bad_timestamp(self):
        payload = {
            "conversation_id": "conv-101",
            "turns": [{"speaker": "agent", "text": "hi", "timestamp": "not-a-date"}],
        }
        errors = validate_conversation_payload(payload)
        self.assertTrue(any("timestamp" in e for e in errors))

if __name__ == "__main__":
    unittest.main()
