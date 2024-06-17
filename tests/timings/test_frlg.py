import pytest
from gui.timings import frlg

# Basic calculation here is load into game time + encounter seq sum
# Snorlax = 9587 + ( 2 * 59 ) = 9705
# TV Time : 1671 + 1000 = 2671
# We get to watch the TV for one second

cases = {
    "FOSSIL": [4248, 6919],
    "STARTERS": [6066, 8737],
    "SNORLAX": [12385, 15056],
    "HYPNO": [10604, 13275],
    "LAPRAS": [4575, 7246],
    "MAGIKARP": [5479, 8150],
    "TOGEPI": [8171, 10842],
    "ABRA": [6822, 9493],
    "CLEFAIRY": [6941, 9612],
    "DRATINI": [7060, 9731],
    "SCYPIN": [7179, 9850],
    "PORYGON": [7298, 9969],
    "SWEET SCENT": [5775, 8446]
}


def create_test_cases() -> list[tuple[list, int, int]]:
    results = []
    for key, vals in cases.items():
        seq = frlg.pokemon_encounters[key]
        results.append((seq, 0, vals[0]))
        results.append((seq, 1000, vals[1]))
    return results


@pytest.mark.parametrize("seq, tv, expected", create_test_cases())
def test_frlg_timer_seq(seq, tv, expected) -> None:
    result = frlg.sum_timer_seq(seq=seq, tv=tv)
    assert result == expected
