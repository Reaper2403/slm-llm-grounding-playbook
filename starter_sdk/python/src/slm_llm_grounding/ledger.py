from __future__ import annotations

from copy import deepcopy
from typing import Any


def empty_ledger() -> dict[str, Any]:
    return {
        "version": 0,
        "hard_facts": {
            "primary_entity": None,
            "entity_kind": "none",
            "issue_cues": [],
            "count_confirmed": "unknown",
            "binary_states": {},
            "notes": [],
        },
        "soft_state": {"best_guess": None, "notes": []},
        "priority": {
            "missing_fields": [],
            "next_question_field": None,
            "next_question_goal": None,
            "question_style": "short_open",
            "must_say_next": None,
        },
        "tool_gate": {
            "search_allowed": False,
            "candidate_only": False,
            "confirmed": False,
            "candidate_text": None,
            "needs_confirmation": False,
        },
        "provenance": {
            "last_slm_turn_index": 0,
            "last_slm_run_at": None,
            "slm_job_state": "idle",
        },
    }


def merge_hard_facts(existing: dict[str, Any], incoming: dict[str, Any]) -> dict[str, Any]:
    merged = deepcopy(existing)
    for key, value in incoming.items():
        if value in (None, "", [], {}, "unknown"):
            continue
        merged[key] = value
    return merged


def build_prompt_packet(ledger: dict[str, Any]) -> dict[str, Any]:
    hard = ledger.get("hard_facts") or {}
    priority = ledger.get("priority") or {}
    gate = ledger.get("tool_gate") or {}
    return {
        "version": ledger.get("version", 0),
        "known": {
            "primary_entity": hard.get("primary_entity"),
            "entity_kind": hard.get("entity_kind"),
            "issue_cues": hard.get("issue_cues", []),
            "count_confirmed": hard.get("count_confirmed", "unknown"),
        },
        "missing_fields": priority.get("missing_fields", []),
        "next_question_field": priority.get("next_question_field"),
        "next_question_goal": priority.get("next_question_goal"),
        "question_style": priority.get("question_style", "short_open"),
        "location_search_allowed": gate.get("search_allowed", False),
        "candidate_needs_confirmation": gate.get("needs_confirmation", False),
        "must_say_next": priority.get("must_say_next"),
        "blocked_actions": [] if gate.get("search_allowed") else ["do_not_resolve_entity_yet"],
    }
