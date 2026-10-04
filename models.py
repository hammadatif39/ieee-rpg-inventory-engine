class Item:
    def __init__(self, name, item_type, value, rarity):
        self.name = name
        self.item_type = item_type
        self.value = int(value)
        self.rarity = rarity

    def __str__(self):
        return f"{self.name} [{self.rarity} {self.item_type}] - {self.value} Gold"

class Weapon(Item):
    def __init__(self, name, value, rarity):
        super().__init__(name, "Weapon", value, rarity)

class Potion(Item):
    def __init__(self, name, value, rarity):
        super().__init__(name, "Potion", value, rarity)

class Armor(Item):
    def __init__(self, name, value, rarity):
        super().__init__(name, "Armor", value, rarity)