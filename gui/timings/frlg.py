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

LOAD_INTO_GAME = 2680
SEED_LOWER_BOUND = 34363
SEED_UPPER_BOUND = 75206
TV_MENU = [553, 1000]
SAVE_SELECT = [3950, 60, 2680]

pokemon_encounters: dict[str, list[int]] = {
    "FOSSIL": [1509],
    "STARTERS": [2095, 1173],
    "SNORLAX": [1006, 8581],
    "HYPNO": [1341, 1090, 1006, 2180, 2012],
    "LAPRAS": [1274, 503],
    "MAGIKARP": [1005, 1676],
    "TOGEPI": [1173, 1006, 1173, 922, 922],
    "ABRA": [2012, 2012],
    "CLEFAIRY": [2012, 2012, 60],
    "DRATINI": [2012, 2012, 60, 60],
    "SCYPIN": [2012, 2012, 60, 60, 60],
    "PORYGON": [2012, 2012, 60, 60, 60, 60],
    "SWEET SCENT": [200, 200, 2000, 200, 200]
}


def get_seq(mon: str) -> list[int]:
    """Returns the sequence list from input string"""
    if mon in ["Bulbasaur", "Squirtle", "Charmander"]:
        mon = "starters"

    if mon in ["Omanyte", "Kabuto", "Aerodactyl"]:
        mon = "fossil"

    if mon in ["Scyther", "Pinsir"]:
        mon = "scypin"

    mon = mon.upper()
    if mon in pokemon_encounters:
        return pokemon_encounters[mon]
    return [0]


def sum_timer_seq(seq: list[int], tv: int) -> int:
    """Returns the sum of timer values based on selected encounter"""
    tvms = sum(TV_MENU) + len(TV_MENU) * 59
    tvr = tvms + tv if tv > 0 else 0
    return LOAD_INTO_GAME + tvr + sum(seq) + len(seq) * 59


def check_time_difference(enc: int, intro: int, total: int) -> bool:
    """With an offset of roughly 300 MS, check to see if the
    total time specified by the user exceeds the expected
    encounter sequence time"""
    offset = 300
    open_sav = sum(SAVE_SELECT) + len(SAVE_SELECT) * 59
    return (total - offset) - (enc + intro + open_sav) > 0
