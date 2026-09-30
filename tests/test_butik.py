import pytest

from butik.lager import MAX_LAGER, Lager
from butik.priser import pris_med_moms, rabatt
from butik.rapport import dagens_summa


def test_moms():
    assert pris_med_moms(100) == 125.0


def test_rabatt():
    assert rabatt(200, 10) == 180.0


def test_lager_fullt():
    lager = Lager()
    with pytest.raises(ValueError):
        lager.add("bok", MAX_LAGER + 1)


def test_summa():
    assert dagens_summa([("a", 100), ("b", 200)]) == 375.0
