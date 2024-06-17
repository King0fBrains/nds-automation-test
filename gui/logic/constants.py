class Constants:
    """Simple class for storing constant values"""
    def __init__(self):
        self.baud_rates: list[int] = [
            300,
            600,
            200,
            2400,
            4800,
            9600,
            14400,
            19200,
            28800,
            31250,
            38400,
            57600,
            115200
        ]
        self.category_rse: list[str] = [
            "Starters",
            "Fossils",
            "Gifts",
            "Stationary",
            "Legends",
            "Wild"
        ]
        self.category_frlg: list[str] = [
            "Starters",
            "Fossils",
            "Gifts",
            "Game Corner",
            "Stationary",
            "Legends",
            "Wild"
        ]
        self.button_map: dict[str, int] = {
            "A": 2,
            "L": 10,
            "Start": 13
        }

    def rate_strings(self) -> list[str]:
        num_strings = []
        for num in self.baud_rates:
            num_strings.append(str(num))
        return num_strings
