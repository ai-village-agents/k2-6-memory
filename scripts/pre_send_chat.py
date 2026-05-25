#!/usr/bin/env python3
"""Executable pre-send chat guard for Kimi K2.6.

Exits 0 on PASS, 4 on BLOCK (matches peer convention).
Usage:
    python3 scripts/pre_send_chat.py --draft "Hello world" --latest-event "..."
"""
import argparse
import sys
import re


def normalize(text: str) -> str:
    return " ".join(text.lower().split())


def shared_sentences(a: str, b: str, min_words: int = 5) -> bool:
    """Return True if any sentence of at least min_words appears in both a and b."""
    def sentences(text):
        # Split on sentence boundaries
        parts = re.split(r'[.!?\n]+', text)
        for part in parts:
            words = part.strip().split()
            if len(words) >= min_words:
                yield " ".join(words)
    a_sents = list(sentences(a))
    b_sents = list(sentences(b))
    for s in a_sents:
        for t in b_sents:
            if s in t or t in s:
                return True
    return False


def main():
    parser = argparse.ArgumentParser(description="Pre-send duplicate-chat guard")
    parser.add_argument("--draft", required=True, help="Message you intend to send")
    parser.add_argument("--latest-event", default="", help="Most recent event text from session prompt")
    args = parser.parse_args()

    draft = args.draft.strip()
    if len(draft) < 10:
        print("BLOCK: Draft too short or empty.")
        sys.exit(4)

    norm_draft = normalize(draft)
    norm_event = normalize(args.latest_event)

    if norm_event:
        if norm_draft in norm_event or norm_event in norm_draft:
            print("BLOCK: Draft matches or is contained in the latest event (possible duplicate).")
            sys.exit(4)

        if "kimi k2.6" in norm_event and shared_sentences(draft, args.latest_event):
            print("BLOCK: Draft shares sentences with recent Kimi K2.6 AGENT_TALK.")
            sys.exit(4)

    print("PASS: No duplicate detected.")
    print()
    print("STALE-PASS WARNING: If any new events arrived after this check, RE-SCAN before sending.")
    sys.exit(0)


if __name__ == "__main__":
    main()
