import reflex as rx
from typing import TypedDict


class Stat(TypedDict):
    name: str
    value: int
    color: str

class Item():
    name: str = ""
    rarity: str = ""
    weight: float = 0.0
    value: str = ""
    category: str = ""
    description: str = ""

    def __init__(self, name: str, rarity: str, weight: float, value: str, category: str, description: str):
        self.name = name
        self.rarity = rarity
        self.weight = weight
        self.value = value
        self.category = category
        self.description = description

class Weapon():
    name: str = ""
    martial: bool = False
    damage: str = ""
    damageType: str = ""
    rarity: str = ""
    tags: str = ""
    weight: float = 0.0
    value: str = ""
    description: str = ""

    def __init__(self, name: str, martial: bool, damage: str, damageType: str, rarity: str, tags: str, weight: float, value: str, description: str):
        self.name = name
        self.martial = martial
        self.damage = damage
        self.damageType = damageType
        self.rarity = rarity
        self.tags = tags
        self.weight = weight
        self.value = value
        self. description = description

class Armor():
    name: str = ""
    weightClass: str = ""
    AC: str = ""
    rarity: str = ""
    weight: float = 0.0
    value: str = ""
    description: str = ""

    def __init__(self, name: str, weightClass: str, AC: str, rarity: str, weight: float, value: str, description: str):
        self.name = name
        self.weightClass = weightClass
        self.AC = AC
        self.rarity = rarity
        self.weight = weight
        self.value = value
        self.description = description



class AppState(rx.State):
    """The app state."""

    character_name: str = "CHARACTER NAME"
    character_race: str = "CHARACTER RACE"
    level: int = 1
    stats: list[Stat] = [
        {"name": "STR", "value": 10, "color": "red"},
        {"name": "DEX", "value": 12, "color": "orange"},
        {"name": "CON", "value": 14, "color": "yellow"},
        {"name": "INT", "value": 8, "color": "green"},
        {"name": "WIS", "value": 15, "color": "blue"},
        {"name": "CHA", "value": 16, "color": "purple"},
    ]

    consumableData = [
        Item(name="Potion of Healing", rarity="Common", weight=0.5, value="50 GP", category="potion", description="You regain 2d4+2 hit points when you drink this potion. Drinking or administering a potion takes an action"),
        Item(name="Arrow", rarity="None", weight=0.05, value="10 CP", category="ammunition", description="You can use a weapon that has the ammunition property to make a ranged attack only if you have ammunition to fire from the weapon. Each time you attack with the weapon, you expend one piece of ammunition. Drawing the ammunition from a quiver, case, or other container is part of the attack (you need a free hand to load a one-handed weapon). At the end of the battle, you can recover half your expended ammunition by taking a minute to search the battlefield.")
    ]

    basicData = [
        Item(name="Dice Set", rarity="None", weight=0.0, value="1 SP", category="tool", description="A standard set of dice. If you are proficient with this gaming set, you may add your proficiency bonus to any ability checks made to play with this gaming set."),
        Item(name="Thieves' Tools", rarity="None", weight=0.0, value="1 SP", category="tool", description="This set of tools includes a small file, a set of lock picks, a small mirror mounted on a metal handle, a set of narrow-bladed scissors, and a pair of pliers. Proficiency with these tools lets you add your proficiency bonus to any ability checks you make to disarm traps or open locks.")
    ]

    weaponData = [
        Weapon(name="Shortsword", martial=True, damage="1d6", damageType="piercing", rarity="Common", tags="Finesse, Light", weight=2, value="10 GP", description="A light, easy to use shortsword."),
        Weapon(name="Quarterstaff", martial=True, damage="1d6", damageType="bludgeoning", rarity="Common", tags="Versatile", weight=4, value="2 SP", description="A simple staff.")
    ]

    armorData = [
        Armor(name="Leather Armor", weightClass="Light", AC="11 + Dex", rarity="Common", weight=10, value="10 GP", description="A set of sturdy leather armor."),
        Armor(name="Plate Armor", weightClass="Heavy", AC="18", rarity="Common", weight=65, value="1500 GP", description="Plate consists of shaped, interlocking metal plates to cover the entire body. A suit of plate includes gauntlets, heavy leather boots, a visored helmet, and thick layers of padding underneath the armor. Buckles and straps distribute the weight over the body. Imposes disadvantage on Stealth rolls while worn, and requires a minimum Strength score of 15 to wear.")
    ]


class AddCustomItemState(rx.State):
    """The current state of the user trying to add a custom item and all the fields to keep track of."""

class AddCustomWeaponState(rx.State):
    """The current state of the user trying to add a custom weapon and all the fields to keep track of."""

class AddCustomArmorState(rx.State):
    """The current state of the user trying to add a custom weapon and all the fields to keep track of."""