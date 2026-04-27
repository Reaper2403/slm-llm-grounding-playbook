from __future__ import annotations

import re


_TRIVIAL = re.compile(r"^(?:yes|no|ok|okay|hello|hi|uh|um|hmm)\W*$", re.IGNORECASE)
_HIGH_SIGNAL = re.compile(
    r"\b(?:fire|smoke|bleeding|not breathing|gun|weapon|trapped|stuck|address|street|avenue|strasse|straße)\b",
    re.IGNORECASE,
)
_CORRECTION = re.compile(r"\b(?:actually|sorry|not\b(?!\s*$)|no\b(?!\s*$)|correction)\b", re.IGNORECASE)


def is_trivial_turn(text: str) -> bool:
    return bool(_TRIVIAL.match((text or "").strip()))


def is_high_signal_turn(text: str) -> bool:
    return bool(_HIGH_SIGNAL.search(text or "")) or bool(_CORRECTION.search(text or ""))


def should_schedule_slm(*, text: str, substantive_turns_since_last_run: int) -> bool:
    if is_trivial_turn(text):
        return False
    if is_high_signal_turn(text):
        return True
    return substantive_turns_since_last_run >= 2
