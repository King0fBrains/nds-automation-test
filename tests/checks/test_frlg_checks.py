# Here all we are checking is to make sure that the total timer
# Exceeds the encounter sum with the lowest possible intro timer
# with a default delay of 10 seconds.

import pytest
from gui.timings import frlg

default_intro = 35000
total_offset = 10000

# These values are taken from the timings test
enc_table = {
    "FOSSIL": 4248,
    "STARTERS": 6066,
    "SNORLAX": 12385,
    "HYPNO": 10604,
    "LAPRAS": 4575,
    "MAGIKARP": 5479,
    "TOGEPI": 8171,
    "ABRA": 6822,
    "CLEFAIRY": 6941,
    "DRATINI": 7060,
    "SCYPIN": 7179,
    "PORYGON": 7298,
    "SWEET SCENT": 5775
}


def create_test_cases() -> list[tuple[int, int, int, bool]]:
    result = []
    for enc in enc_table.values():
        calc = enc + total_offset + default_intro
        case = (enc, default_intro, calc, True)
        result.append(case)
    return result


@pytest.mark.parametrize("enc, intro, total, expected", create_test_cases())
def test_frlg_timer_difference(enc: int, intro: int, total: int, expected: bool) -> None:
    result = frlg.check_time_difference(enc, intro, total)
    assert result == expected
