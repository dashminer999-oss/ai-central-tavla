"""Kvitton."""

from .config import VALUTA


def formatera_rad(namn: str, pris: float) -> str:
    return f"{namn}: {pris:.2f} {VALUTA}"


def formatera_kvitto(rader: list[tuple[str, float]]) -> str:
    return "\n".join(formatera_rad(n, p) for n, p in rader)
