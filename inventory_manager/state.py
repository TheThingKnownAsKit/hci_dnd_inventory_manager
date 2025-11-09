import reflex as rx
from typing import TypedDict, NotRequired


class Stat(TypedDict):
    name: str
    value: int
    bg_class: str

class Item(TypedDict):
    name: str
    rarity: NotRequired[str]
    weight: NotRequired[str]
    value: NotRequired[str]
    category: NotRequired[str]
    description: NotRequired[str]
    quantity: int


class Weapon(TypedDict):
    name: str
    martial: NotRequired[str]
    damage: NotRequired[str]
    damageType: NotRequired[str]
    rarity: NotRequired[str]
    tags: NotRequired[str]
    weight: NotRequired[str]
    value: NotRequired[str]
    description: NotRequired[str]
    quantity: int


class Armor(TypedDict):
    name: str
    weightClass: NotRequired[str]
    AC: NotRequired[str]
    rarity: NotRequired[str]
    weight: NotRequired[str]
    value: NotRequired[str]
    description: NotRequired[str]
    quantity: int



class AppState(rx.State):
    """The app state."""
    dialog_open: bool = False

    character_name: str = "CHARACTER NAME"
    character_class: str = "CHARACTER CLASS"
    character_subclass: str = "CHARACTER SUBCLASS"
    character_subrace: str = "CHARACTER SUBRACE"
    character_race: str = "CHARACTER RACE"
    character_pp: int = 0
    character_gp: int = 0
    character_ep: int = 0
    character_sp: int = 0
    character_cp: int = 0
    level: int = 1
    stats: list[Stat] = [
        {"name": "STR", "value": 10, "bg_class": "bg-purple-400"},
        {"name": "DEX", "value": 12, "bg_class": "bg-purple-500"},
        {"name": "CON", "value": 14, "bg_class": "bg-purple-400"},
        {"name": "INT", "value": 8, "bg_class": "bg-purple-500"},
        {"name": "WIS", "value": 15, "bg_class": "bg-purple-400"},
        {"name": "CHA", "value": 16, "bg_class": "bg-purple-500"},
    ]

    consumableInv: list[Item] = []
    basicInv: list[Item] = []
    weaponInv: list[Weapon] = []
    armorInv: list[Armor] = []

    def update_stat(self, name: str, new_value: str):
        """Update a character stat by name."""
        updated = []
        for s in self.stats:
            if s["name"] == name:
                try:
                    s = s.copy()  # make a copy to avoid mutating original
                    s["value"] = int(new_value)
                except ValueError:
                    s["value"] = 0
            updated.append(s)
        self.stats = updated

    consumableData: list[Item] = [
        {
            "name": "Potion of Healing",
            "rarity": "Common",
            "weight": "0.5",
            "value": "50 GP",
            "category": "potion",
            "description": "You regain 2d4+2 hit points when you drink this potion. Drinking or administering a potion takes an action.",
            "quantity": 3,
        },
        {
            "name": "Arrow",
            "rarity": "None",
            "weight": "0.05",
            "value": "10 CP",
            "category": "ammunition",
            "description": "You can use a weapon that has the ammunition property to make a ranged attack only if you have ammunition to fire from the weapon. Each time you attack with the weapon, you expend one piece of ammunition. Drawing the ammunition from a quiver, case, or other container is part of the attack. At the end of the battle, you can recover half your expended ammunition by taking a minute to search the battlefield.",
            "quantity": 20,
        },
    ]

    basicData: list[Item] = [
        {
            "name": "Dice Set",
            "rarity": "None",
            "weight": "0.0",
            "value": "1 SP",
            "category": "tool",
            "description": "A standard set of dice. If you are proficient with this gaming set, you may add your proficiency bonus to any ability checks made to play with this gaming set.",
            "quantity": 1,
        },
        {
            "name": "Thieves' Tools",
            "rarity": "None",
            "weight": "0.0",
            "value": "25 GP",
            "category": "tool",
            "description": "This set of tools includes a small file, a set of lock picks, a small mirror mounted on a metal handle, a set of narrow-bladed scissors, and a pair of pliers. Proficiency with these tools lets you add your proficiency bonus to any ability checks you make to disarm traps or open locks.",
            "quantity": 1,
        },
    ]

    weaponData: list[Weapon] = [
        {
            "name": "Shortsword",
            "martial": "True",
            "damage": "1d6",
            "damageType": "piercing",
            "rarity": "Common",
            "tags": "Finesse, Light",
            "weight": "2",
            "value": "10 GP",
            "description": "A light, easy to use shortsword.",
            "quantity": 1,
        },
        {
            "name": "Quarterstaff",
            "martial": "True",
            "damage": "1d6",
            "damageType": "bludgeoning",
            "rarity": "Common",
            "tags": "Versatile",
            "weight": "4",
            "value": "2 SP",
            "description": "A simple staff.",
            "quantity": 1,
        },
    ]

    armorData: list[Armor] = [
        {
            "name": "Leather Armor",
            "weightClass": "Light",
            "AC": "11 + Dex",
            "rarity": "Common",
            "weight": "10",
            "value": "10 GP",
            "description": "A set of sturdy leather armor.",
            "quantity": 1,
        },
        {
            "name": "Plate Armor",
            "weightClass": "Heavy",
            "AC": "18",
            "rarity": "Common",
            "weight": "65",
            "value": "1500 GP",
            "description": "Plate consists of shaped, interlocking metal plates to cover the entire body. A suit of plate includes gauntlets, heavy leather boots, a visored helmet, and thick layers of padding underneath the armor. Buckles and straps distribute the weight over the body. Imposes disadvantage on Stealth rolls while worn, and requires a minimum Strength score of 15 to wear.",
            "quantity": 1,
        },
    ]

    def add_item_to_inv(self, title: str, item):
        """Append an item to the specified category."""
        if title == "WEAPONS":
            self.weaponInv.append(item)
        elif title == "ARMOR":
            self.armorInv.append(item)
        elif title == "CONSUMABLES":
            self.consumableInv.append(item)
        elif title == "BASIC":
            self.basicInv.append(item)
        
        print(item)

class AddCustomItemState(AppState):
    """The current state of the user trying to add a custom item and all the fields to keep track of."""

    name: str
    rarity: str
    weight: str
    value: str
    category: str
    description: str
    quantity: int

    def create_basic_item(self):
        item = Item(
            name=self.name,
            rarity=self.rarity,
            weight=self.weight,
            value=self.value,
            category=self.category,
            description=self.description,
            quantity=self.quantity
        )

        print("Adding basic item")

        self.add_item_to_inv(title="BASIC", item=item)
        self.dialog_open = False
        self = AddCustomItemState
    
    def create_consumable_item(self):
        item = Item(
            name=self.name,
            rarity=self.rarity,
            weight=self.weight,
            value=self.value,
            category=self.category,
            description=self.description,
            quantity=self.quantity
        )

        print("Adding consumable item")

        self.add_item_to_inv(title="CONSUMABLES", item=item)
        self.dialog_open = False
        self = AddCustomItemState

class AddCustomWeaponState(AppState):
    """The current state of the user trying to add a custom weapon and all the fields to keep track of."""

    name: str
    martial: str
    damage: str
    damageType: str
    rarity: str
    tags: str
    weight: str
    value: str
    description: str
    quantity: int

    def create_weapon(self):
        weapon = Weapon(
            name=self.name,
            martial=self.martial,
            damage=self.damage,
            damageType=self.damageType,
            rarity=self.rarity,
            tags=self.tags,
            weight=self.weight,
            value=self.value,
            description=self.description,
            quantity=self.quantity
        )

        self.add_item_to_inv(title="WEAPONS", item=weapon)
        self.dialog_open = False
        self = AddCustomWeaponState

class AddCustomArmorState(AppState):
    """The current state of the user trying to add a custom weapon and all the fields to keep track of."""

    name: str
    weightClass: str
    AC: str
    rarity: str
    weight: str
    value: str
    description: str
    quantity: int

    def create_armor(self):
        armor = Armor(
            name=self.name,
            weightClass=self.weightClass,
            AC=self.AC,
            rarity=self.rarity,
            weight=self.weight,
            value=self.value,
            description=self.description,
            quantity=self.quantity
        )

        self.add_item_to_inv(title="ARMOR", item=armor)
        self.dialog_open = False
        self = AddCustomArmorState