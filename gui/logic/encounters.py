"""Module to store Arduino side logic values and encounter data"""


class RSE:
    """RSE specific encounter data"""
    def __init__(self):
        self.starters: dict[str, int] = {
            "Chikorita": 0,
            "Cyndaquil": 0,
            "Totodile": 0,
            "Mudkip": 9,
            "Torchic": 8,
            "Treecko": 10
        }
        self.fossils: dict[str, int] = {
            "Anorith": 1,
            "Lileep": 1
        }
        self.gifts: dict[str, int] = {
            "Castform": 2,
            "Beldum": 3,
            "Wynaut": 4
        }
        self.stationary: dict[str, int] = {
            "Keckleon": 5,
            "Electrode": 0,
            "Sudowoodo": 6
        }
        self.legends: dict[str, int] = {
            "Regirock": 0,
            "Regice": 0,
            "Registeel": 0,
            "Latias": 0,
            "Latios": 0,
            "Kyogre": 0,
            "Groudon": 0,
            "Rayquaza": 0
        }
        self.wild: dict[str, int] = {
            "Sweet Scent": 7
        }
        self.categories = {
            "starters": self.starters,
            "fossils": self.fossils,
            "gifts": self.gifts,
            "stationary": self.stationary,
            "legends": self.legends,
            "wild": self.wild
        }
        self.category_reqs: dict[str, str] = {
            "Starters": "This operation assumes that:\n"
                        "1. You are standing in front of Professor Birch's bag",
            "Fossils": "This operation assumes that:\n"
                       "1. You have already provided the Scientist with your fossil.\n"
                       "2. You are standing in front of the Scientist ready to "
                       "receive the desired fossil.",
            "Legends": "This operation assumes that you are standing in front of your target.",
            "Gifts": "This operation assumes that you are standing in front of your target.",
            "Stationary": "This operation assumes that you are standing in front of your target.",
            "Wild": "This operation assumes that:\n"
                    "1. You are standing in the desired encounter location\n"
                    "2. The Pokemon with Sweet Scent is in the second slot of your party."

        }

    def get_category_mons(self, category: str) -> list[str]:
        """Return list of static encounters based on category input"""
        category = category.lower()
        if category in self.categories:
            return list(self.categories[category])
        return []

    def get_encounter_value(self, category: str, key: str) -> int:
        """Return encounter value based on category input"""
        cat_dict = self.categories.get(category.lower(), {})
        return cat_dict.get(key, None)


class FRLG:
    """FRLG specific encounter data"""
    def __init__(self):
        self.starters: dict[str, int] = {
            "Bulbasaur": 2,
            "Charmander": 2,
            "Squirtle": 2
        }
        self.fossils: dict[str, int] = {
            "Omanyte": 1,
            "Kabuto": 1,
            "Aerodactyl": 1
        }
        self.gifts: dict[str, int] = {
            "Hitmonlee": 3,
            "Hitmonchan": 3,
            "Magikarp": 4,
            "Lapras": 5,
            "Eevee": 0,
            "Togepi": 6
        }
        self.game_corner: dict[str, int] = {
            "Abra": 8,
            "Clefairy": 9,
            "Pinsir": 10,
            "Scyther": 10,
            "Dratini": 11,
            "Porygon": 12
        }
        self.stationary: dict[str, int] = {
            "Snorlax": 13,
            "Electrode": 0,
            "Hypno": 14
        }
        self.legends: dict[str, int] = {
            "Articuno": 0,
            "Zapdos": 0,
            "Moltres": 0,
            "Mewtwo": 0
        }
        self.wild: dict[str, int] = {
            "Sweet Scent": 7
        }

        self.category_reqs: dict[str, str] = {
            "Starters": "This operation assumes that:\n"
                        "1. You are standing in front of your desired starter.",
            "Fossils": "This operation assumes that:\n"
                       "1. You have already provided the Scientist with your fossil.\n"
                       "2. You are standing in front of the Scientist ready to "
                       "receive the desired fossil.",
            "Legends": "This operation assumes that you are standing in front of your target.",
            "Gifts": "This operation assumes that you are standing in front of your target.",
            "Game Corner": "This operation assumes that:\n"
                           "1. You have enough coins for your desired target.\n"
                           "2. You are standing in front of the Game Corner NPC.",
            "Stationary": "This operation assumes that you are standing in front of your target.",
            "Static": "This operation assumes that you are standing in front of your target.",
            "Wild": "This operation assumes that:\n"
                    "1. You are standing in the desired encounter location\n"
                    "2. Your Pokemon with Sweet Scent is in the second slot of your party.",
        }
        self.categories = {
            "starters": self.starters,
            "fossils": self.fossils,
            "gifts": self.gifts,
            "stationary": self.stationary,
            "game corner": self.game_corner,
            "legends": self.legends,
            "wild": self.wild
        }

    def get_category_mons(self, category: str) -> list[str]:
        """Return list of static encounters based on category input"""
        category = category.lower()
        if category in self.categories:
            return list(self.categories[category])
        return []

    def get_encounter_value(self, category: str, key: str) -> int:
        """Return encounter value based on category input"""
        cat_dict = self.categories.get(category.lower(), {})
        return cat_dict.get(key, None)
