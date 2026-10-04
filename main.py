import os
from models import Item, Weapon, Potion, Armor

class Inventory:
    def __init__(self):
        self.items = []

    def load_from_csv(self, filepath):
        try:
            with open(filepath, 'r') as file:
                next(file)  # Skip header
                for line in file:
                    try:
                        # Attempt to parse data
                        parts = line.strip().split(',')
                        if len(parts) != 4:
                            raise ValueError("Incorrect number of columns")
                        
                        name, item_type, value, rarity = parts
                        
                        # Apply OOP Inheritance by instantiating specific child classes
                        if item_type == "Weapon":
                            self.items.append(Weapon(name, value, rarity))
                        elif item_type == "Potion":
                            self.items.append(Potion(name, value, rarity))
                        elif item_type == "Armor":
                            self.items.append(Armor(name, value, rarity))
                        else:
                            self.items.append(Item(name, item_type, value, rarity))
                            
                    except ValueError as e:
                        print(f"[WARNING] Corrupted row skipped: '{line.strip()}' -> {e}")
        except FileNotFoundError:
            print("Critical Error: items.csv not found!")
        finally:
            print("[SYSTEM] File parsing attempt finished.\n")

    def display_all(self):
        for item in self.items:
            print(item)

    def total_gold_value(self):
        return sum(item.value for item in self.items)

    def get_categories(self):
        # Uses a Set to extract unique categories
        return {item.item_type for item in self.items}

    def get_organized_inventory(self):
        # Nested Dictionary organizing items by their category
        organized = {}
        for item in self.items:
            if item.item_type not in organized:
                organized[item.item_type] = []
            organized[item.item_type].append(item.name)
        return organized

    def filter_epic_items(self):
        # List comprehension for fast filtering
        return [item for item in self.items if item.rarity == "Epic"]

def main():
    print("--- RPG Inventory Engine Booting ---")
    player_inv = Inventory()
    
    # 1. File Handling & Error Catching
    player_inv.load_from_csv("data/items.csv")

    # 2. Display Parsed Objects
    print("--- All Valid Items ---")
    player_inv.display_all()

    # 3. Analytics
    print(f"\n--- Total Inventory Value ---")
    print(f"{player_inv.total_gold_value()} Gold")
    
    # 4. Sets
    print(f"\n--- Unique Item Categories (Set) ---")
    print(player_inv.get_categories())

    # 5. Nested Dictionaries
    print("\n--- Organized Inventory (Nested Dict) ---")
    organized = player_inv.get_organized_inventory()
    for category, items in organized.items():
        print(f"{category}: {', '.join(items)}")

    # 6. List Comprehension
    print("\n--- Epic Gear Filter (List Comprehension) ---")
    epic_items = player_inv.filter_epic_items()
    for e in epic_items:
        print(e)

if __name__ == "__main__":
    main()