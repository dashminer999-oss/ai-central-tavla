"""Rapporter."""

from .priser import pris_med_moms


def dagens_summa(rader: list[tuple[str, float]]) -> float:
    """Summan av dagens försäljning inklusive moms."""
    return round(sum(pris_med_moms(p) for _, p in rader), 2)
