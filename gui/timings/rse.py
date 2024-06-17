"""
This module stores data specific to the Arduino code
Each value is an estimate and was determined by using
and emulator and Lua scripts. These can be more efficient,
but it is helpful to overshoot timings as to not miss
the target. This data is important because if we didn't
check to see if the user input was shorter than it takes
the Arduino to physically complete a sequence, it may result in
an overflow or out of bounds error producing delay times that
exceed literal hours and or days
"""


LOAD_INTO_GAME = 2263
DEAD_BATTERY: list[int] = [4191, 838, 355, 3353, 1760, 335]
LIVE_BATTERY: list[int] = [4191, 838, 355, 3353]
BATTLE_RECORD: list[int] = [200, 200, 200, 200, 200, 800, 700, 300, 3823, 2200, 1200]

pokemon_encounters: dict[str, list[int]] = {
    "CASTFORM": [645],
    "BELDUM": [838, 754],
    "WYNAUT": [1375, 1190, 1190, 2084, 1592, 1592],
    "FOSSIL": [671, 1157],
    "KECKLEON": [1911, 536, 587, 1190],
    "SUDOWOODO": [3017, 671],
    "TORCHIC": [1406],
    "MUDKIP": [1406, 251],
    "TREECKO": [1406, 251],
    "SWEET SCENT": [200, 200, 1676, 200, 200]
}


def get_seq(mon: str) -> list[int]:
    """Returns the sequence list from input string"""
    if mon in ["Anorith", "Lileep"]:
        mon = "fossil"
    mon = mon.upper()
    if mon in pokemon_encounters:
        return pokemon_encounters[mon]
    return [0]


def sum_timer_seq(seq: list[int], battery: bool = False, record: bool = False) -> int:
    """Returns the sum of timer values based on selected encounter"""
    br = [] if not record else BATTLE_RECORD
    br = len(br) * 59 + sum(br)
    batt = LIVE_BATTERY if battery else DEAD_BATTERY
    batt = len(batt) * 59 + sum(batt)
    return LOAD_INTO_GAME + batt + sum(seq) + br + len(seq) * 59


def check_time_difference(enc: int, total: int) -> bool:
    """With an offset of roughly 300 MS, check to see if the
    total time specified by the user exceeds the expected
    encounter sequence time"""
    offset = 300
    return (total - offset) - enc > 0
