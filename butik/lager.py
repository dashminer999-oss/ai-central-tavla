"""Lagersaldo."""

MAX_LAGER = 500


class Lager:
    def __init__(self) -> None:
        self._saldo: dict[str, int] = {}

    def add(self, artikel: str, antal: int) -> None:
        """Lägg in antal av en artikel. Totalen får inte passera MAX_LAGER."""
        ny = self._saldo.get(artikel, 0) + antal
        if ny > MAX_LAGER:
            raise ValueError("lagret är fullt")
        self._saldo[artikel] = ny

    def remove(self, artikel: str, antal: int) -> None:
        """Ta ut antal av en artikel."""
        if self._saldo.get(artikel, 0) < antal:
            raise ValueError("finns inte så många i lager")
        self._saldo[artikel] -= antal

    def saldo(self, artikel: str) -> int:
        return self._saldo.get(artikel, 0)
