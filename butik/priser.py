"""Prisberäkningar."""

from .config import AVRUNDNING

MOMS_SATS = 0.25


def pris_med_moms(pris: float) -> float:
    """Priset inklusive moms, avrundat enligt AVRUNDNING."""
    return round(pris * (1 + MOMS_SATS), AVRUNDNING)


def rabatt(pris: float, procent: float) -> float:
    """Priset efter en procentuell rabatt."""
    return round(pris * (1 - procent / 100), AVRUNDNING)
