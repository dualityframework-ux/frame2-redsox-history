from __future__ import annotations

from typing import Literal

Tone = Literal["simple", "analytical", "one-liner"]


def _clean(value: str) -> str:
    return " ".join(str(value).strip().split())


def build_post_variants(insight: dict, tone: Tone = "simple") -> str:
    """
    Convert an insight dict into one clean post string.

    Expected insight shape:
    {
        "observation": "...",
        "mechanism": "...",
        "implication": "...",
        "tag": "..."
    }
    """

    observation = _clean(insight.get("observation", "the game shifted."))
    mechanism = _clean(insight.get("mechanism", "one hidden edge started winning repeatedly."))
    implication = _clean(insight.get("implication", "the scoreboard usually follows the process."))
    tag = _clean(insight.get("tag", "signal"))

    if tone == "simple":
        return (
            f"fans see: {observation}\n\n"
            f"frame² sees: {mechanism}\n\n"
            f"implication: {implication}"
        )

    if tone == "analytical":
        return (
            f"observation: {observation}\n"
            f"mechanism: {mechanism}\n"
            f"implication: {implication}\n"
            f"tag: {tag}"
        )

    if tone == "one-liner":
        return f"fans see: {observation} frame² sees: {mechanism} implication: {implication}"

    return (
        f"fans see: {observation}\n\n"
        f"frame² sees: {mechanism}\n\n"
        f"implication: {implication}"
    )
