import pytest
from gui.timings import rse

# All sequence integers are represent time in milliseconds
# There is a lot of room for improving the accuracy of timing sequences. All the delay values
# Were estimated using Lua Scripts and an emulator. Most of these delays are longer than needed
# To ensure that the encounters actually get processed correctly
# The sequences are formatted as lists because that is how they are processed in the Arduino side
# Making changes to a specific delay sequence is easier than running sums every time manually

# A sum timer sequences is calculated by summing the encounter sequence steps
# In rse.pokemon_encounters["BELDUM"] for example, [838, 754] represent delay times
# followed by A presses. Each A press consumes 59 MS. Therefor the calculation would be
# len(rse.pokemon_encounters["BELDUM"]) * 59 + sum(rse.pokemon_encounters["BELDUM"]
# Then the time it takes to load into the game (2263) and the time it takes
# To skip through the dead/live battery sequence is added to the encounter sequence sum
# If the battle record method is used, that sequence sum is added to the total

# The fastest encounters are the ones that require a single A press (Legends, etc.)
# From small tests using the Arduino, the observed average for getting into the game and in front of the
# Single A press target is about 13520 MS, or 13.5 seconds if the cartridge has a dead battery.

# Note: the dead/live battery sequence accounts for the RSE intro cutscenes
# If the total time (target advance) is shorter than the time it takes to actually get
# To the encounter, the Microcontroller will produce some sort of buffer overflow or out-of-bounds
# Error, typically resulting in delay times that exceed multiple hours.
# Luckily, the Arduino Has a reset button

# Load into game = 2263

# Live Battery Sum = 8737 + ( 4 * 59 ) = 8973
# Dead Battery Sum = 10832 + ( 6 * 59 ) = 11186

# Battle Record Sum = 10023 + ( 11 * 59 ) = 10672

# Castform sum = 645 + ( 1 * 59 ) = 704
# Beldum sum = 1592 + ( 2 * 59 ) = 1710
# Wynaut sum = 9023 + ( 6 * 59 ) = 9377
# Fossil sum = 1828 + ( 2 * 59 ) = 1946
# Keckleon sum = 4224 + (4 * 59 ) = 4460
# Sudowoodo sum = 3688 + ( 2 * 59 ) = 3806
# Torchic sum = 1406 + ( 1 * 59 ) = 1465
# Mudkip sum = 1657 + ( 2 * 59 ) = 1175
# Treecko sum = 1657 + ( 2 * 59 ) = 1175
# Sweet Scent sum = 2476 + (5 * 59) = 2771


cases = {
    "WYNAUT": [22826, 20613, 33498, 31285],
    "BELDUM": [15159, 12946, 25831, 23618],
    "CASTFORM": [14153, 11940, 24825, 22612],
    "FOSSIL": [15395, 13182, 26067, 23854],
    "KECKLEON": [17909, 15696, 28581, 26368],
    "SUDOWOODO": [17255, 15042, 27927, 25714],
    "TORCHIC": [14914, 12701, 25586, 23373],
    "MUDKIP": [15224, 13011, 25896, 23683],
    "TREECKO": [15224, 13011, 25896, 23683],
    "SWEET SCENT": [16220, 14007, 26892, 24679],
}

options = [(False, False), (True, False), (False, True), (True, True)]


def create_test_cases() -> list[tuple[list, bool, bool, int]]:
    result = []
    for key in cases.keys():
        zipper = zip(cases[key], options)
        for option in zipper:
            seq = rse.pokemon_encounters[key]
            result.append((seq, option[1][0], option[1][1], option[0]))
    return result


@pytest.mark.parametrize(
    "seq, battery, record, expected",
    create_test_cases(),
)
def test_rse_timer_seq(seq, battery, record, expected) -> None:
    result = rse.sum_timer_seq(seq=seq, battery=battery, record=record)
    assert result == expected
