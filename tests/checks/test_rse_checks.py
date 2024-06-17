import pytest
from gui.timings import rse

total_offset = 10000

enc_table = {
    "WYNAUT": 22826,
    "BELDUM": 15159,
    "CASTFORM": 14153,
    "FOSSIL": 15395,
    "KECKLEON": 17909,
    "SUDOWOODO": 17255,
    "TORCHIC": 14914,
    "MUDKIP": 15224,
    "TREECKO": 15224,
    "SWEET SCENT": 16220
}


def create_test_cases() -> list[tuple[int, int, bool]]:
    result = []
    for enc in enc_table.values():
        calc = enc + total_offset
        case = (enc, calc, True)
        result.append(case)
    return result


@pytest.mark.parametrize("enc, total, expected", create_test_cases())
def test_rse_timer_difference(enc: int, total: int, expected: bool) -> None:
    result = rse.check_time_difference(enc, total)
    assert result == expected
