import reflex as rx
from typing import TypedDict, NotRequired


class Stat(TypedDict):
    name: str
    value: int
    bg_class: str

class Item(TypedDict):
    name: str
    itemID: int
    rarity: NotRequired[str]
    weight: NotRequired[str]
    value: NotRequired[str]
    category: NotRequired[str]
    description: NotRequired[str]
    quantity: int
    type: str


class Weapon(TypedDict):
    name: str
    itemID: int
    martial: NotRequired[str]
    damage: NotRequired[str]
    damageType: NotRequired[str]
    rarity: NotRequired[str]
    tags: NotRequired[str]
    weight: NotRequired[str]
    value: NotRequired[str]
    description: NotRequired[str]
    quantity: int
    type: str


class Armor(TypedDict):
    name: str
    itemID: int
    weightClass: NotRequired[str]
    AC: NotRequired[str]
    rarity: NotRequired[str]
    weight: NotRequired[str]
    value: NotRequired[str]
    description: NotRequired[str]
    quantity: int
    type: str



class AppState(rx.State):
    """The app state."""
    dialog_open: bool = False
    selected_item_ID: int = 0
    selected_item_type: str = ""
    nextCustomID: int = 9000

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
    infoHeader: str = "No Item Selected"
    infoSubheader: str = ""
    infoBlock: str = ""
    infoQuantity: str = ""
    stats: list[Stat] = [
        {"name": "STR", "value": 10, "bg_class": "bg-purple-400"},
        {"name": "DEX", "value": 10, "bg_class": "bg-purple-500"},
        {"name": "CON", "value": 10, "bg_class": "bg-purple-400"},
        {"name": "INT", "value": 10, "bg_class": "bg-purple-500"},
        {"name": "WIS", "value": 10, "bg_class": "bg-purple-400"},
        {"name": "CHA", "value": 10, "bg_class": "bg-purple-500"},
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

    # Each item has an ID based on its class
    # Weapons: 1000-1999
    # Armor: 2000-2999
    # Consummables: 3000-5999
    # Basic: 6000-8999
    # Custom: >= 9000

    consumableData: list[Item] = [
        {
            "name": "Potion of Healing",
            "itemID": 3000,
            "rarity": "Common",
            "weight": "0.5",
            "value": "50 GP",
            "category": "potion",
            "description": "You regain 2d4+2 hit points when you drink this potion. Drinking or administering a potion takes an action.",
            "quantity": 1,
            "type": "consumable",
        },
        {
            "name": "Arrow",
            "itemID": 3001,
            "rarity": "None",
            "weight": "0.05",
            "value": "10 CP",
            "category": "ammunition",
            "description": "You can use a weapon that has the ammunition property to make a ranged attack only if you have ammunition to fire from the weapon. Each time you attack with the weapon, you expend one piece of ammunition. Drawing the ammunition from a quiver, case, or other container is part of the attack. At the end of the battle, you can recover half your expended ammunition by taking a minute to search the battlefield.",
            "quantity": 1,
            "type": "consumable",
        },
    ]

    basicData: list[Item] = [
        {
            "name": "Dice Set",
            "itemID": 6000,
            "rarity": "None",
            "weight": "0.0",
            "value": "1 SP",
            "category": "tool",
            "description": "A standard set of dice. If you are proficient with this gaming set, you may add your proficiency bonus to any ability checks made to play with this gaming set.",
            "quantity": 1,
            "type": "basic",
        },
        {
            "name": "Thieves' Tools",
            "itemID": 6001,
            "rarity": "None",
            "weight": "0.0",
            "value": "25 GP",
            "category": "tool",
            "description": "This set of tools includes a small file, a set of lock picks, a small mirror mounted on a metal handle, a set of narrow-bladed scissors, and a pair of pliers. Proficiency with these tools lets you add your proficiency bonus to any ability checks you make to disarm traps or open locks.",
            "quantity": 1,
            "type": "basic",
        },
    ]

    weaponData: list[Weapon] = [
        {
            "name": "Shortsword",
            "itemID": 1000,
            "martial": "True",
            "damage": "1d6",
            "damageType": "piercing",
            "rarity": "Common",
            "tags": "Finesse, Light",
            "weight": "2",
            "value": "10 GP",
            "description": "A light, easy to use shortsword.",
            "quantity": 1,
            "type": "weapon",
        },
        {
            "name": "Quarterstaff",
            "itemID": 1001,
            "martial": "True",
            "damage": "1d6",
            "damageType": "bludgeoning",
            "rarity": "Common",
            "tags": "Versatile",
            "weight": "4",
            "value": "2 SP",
            "description": "A simple staff.",
            "quantity": 1,
            "type": "weapon",
        },
    ]

    armorData: list[Armor] = [
        {
            "name": "Leather Armor",
            "itemID": 2000,
            "weightClass": "Light",
            "AC": "11 + Dex",
            "rarity": "Common",
            "weight": "10",
            "value": "10 GP",
            "description": "A set of sturdy leather armor.",
            "quantity": 1,
            "type": "armor",
        },
        {
            "name": "Plate Armor",
            "itemID": 2001,
            "weightClass": "Heavy",
            "AC": "18",
            "rarity": "Common",
            "weight": "65",
            "value": "1500 GP",
            "description": "Plate consists of shaped, interlocking metal plates to cover the entire body. A suit of plate includes gauntlets, heavy leather boots, a visored helmet, and thick layers of padding underneath the armor. Buckles and straps distribute the weight over the body. Imposes disadvantage on Stealth rolls while worn, and requires a minimum Strength score of 15 to wear.",
            "quantity": 1,
            "type": "armor",
        },
    ]

    def add_item_to_inv(self, title: str, item):
        """Append an item to the specified category."""
        if title == "WEAPONS":
            if self.weaponInv is not None:
                for i in self.weaponInv:
                    if i["itemID"] == item["itemID"]:
                        i["quantity"] = i["quantity"] + 1
                        if i["itemID"] == self.selected_item_ID:
                            self.refresh_item_quantity(i)
                        return
            
            self.weaponInv.append(item)
        elif title == "ARMOR":
            if self.armorInv is not None:
                for i in self.armorInv:
                    if i["itemID"] == item["itemID"]:
                        i["quantity"] = i["quantity"] + 1
                        if i["itemID"] == self.selected_item_ID:
                            self.refresh_item_quantity(i)
                        return
            self.armorInv.append(item)
        elif title == "CONSUMABLES":
            if self.consumableInv is not None:
                for i in self.consumableInv:
                    if i["itemID"] == item["itemID"]:
                        i["quantity"] = i["quantity"] + 1
                        if i["itemID"] == self.selected_item_ID:
                            self.refresh_item_quantity(i)
                        return
            self.consumableInv.append(item)
        elif title == "BASIC":
            if self.basicInv is not None:
                for i in self.basicInv:
                    if i["itemID"] == item["itemID"]:
                        i["quantity"] = i["quantity"] + 1
                        if i["itemID"] == self.selected_item_ID:
                            self.refresh_item_quantity(i)
                        return
            self.basicInv.append(item)
        
        print(item)

    def iterate_quantity_up(self):
        workingItem = self.selected_item_ID
        workingType = self.selected_item_type

        if workingType == "basic":
            workingList = self.basicInv
        elif workingType == "consumable":
            workingList = self.consumableInv
        elif workingType == "weapon":
            workingList = self.weaponInv
        elif workingType == "armor":
            workingList = self.armorInv

        for i in workingList:
                    if i["itemID"] == workingItem:
                        i["quantity"] = i["quantity"] + 1
                        self.refresh_item_quantity(i)
        

    def iterate_quantity_down(self):
        workingItem = self.selected_item_ID
        workingType = self.selected_item_type

        if workingType == "basic":
            workingList = self.basicInv
        elif workingType == "consumable":
            workingList = self.consumableInv
        elif workingType == "weapon":
            workingList = self.weaponInv
        elif workingType == "armor":
            workingList = self.armorInv

        for i in workingList:
                    if i["itemID"] == workingItem:
                        i["quantity"] = i["quantity"] - 1
                        if i["quantity"] <= 0:
                            self.remove_item()
                            return
                        self.refresh_item_quantity(i)

    def remove_item(self):
        workingItem = self.selected_item_ID
        workingType = self.selected_item_type

        if workingType == "basic":
            workingList = self.basicInv
        elif workingType == "consumable":
            workingList = self.consumableInv
        elif workingType == "weapon":
            workingList = self.weaponInv
        elif workingType == "armor":
            workingList = self.armorInv

        j = 0
        for i in workingList:
                    
                    if i["itemID"] == workingItem:
                        workingList.pop(j)
                    j = j+1

        self.selected_item_ID = 0
        self.selected_item_type = ""
        self.infoHeader = "No Item Selected"
        self.infoSubheader = ""
        self.infoBlock = ""
        self.infoQuantity = ""
        return



    def check_item_information(self, item):
        item_id = item["itemID"]

    # --- Toggle behavior ---
        if self.selected_item_ID == item_id:
            # Clicking the same item again → clear info
            self.selected_item_ID = 0
            self.selected_item_type = ""
            self.infoHeader = "No Item Selected"
            self.infoSubheader = ""
            self.infoBlock = ""
            self.infoQuantity = ""
            return

        # Otherwise → show the new item
        self.selected_item_ID = item_id
        self.selected_item_type = item["type"]

        if item["type"] == "basic" or item["type"] == "consumable":
            self.infoHeader = item["name"]
            self.infoSubheader = item["category"]
            self.infoBlock = "Category: " + item["category"] + "\nRarity: " + item["rarity"] + "\nValue: " + item["value"] + "\nWeight: " + item["weight"] + "\n\n" + item["description"] + "\n\n"
            self.infoQuantity = "Quantity: " + str(item["quantity"])
        elif item["type"] == "weapon":
            self.infoHeader = item["name"]
            if item["martial"] == "True":
                self.infoSubheader = "martial weapon"
            elif item["martial"] == "False":
                self.infoSubheader = "simple weapon"
            self.infoBlock = "Damage: " + item["damage"] + "\nDamage Type: " + item["damageType"] + "\nRarity: " + item["rarity"] + "\nValue: " + item["value"] + "\nProperties: " + item["tags"] + "\nWeight: " + item["weight"] + "\n\n" + item["description"] + "\n\n"
            self.infoQuantity = "Quantity: " + str(item["quantity"])
        elif item["type"] == "armor":
            self.infoHeader = item["name"]
            self.infoSubheader = item["weightClass"] + " armor"
            self.infoBlock = "AC: " + item["AC"] + "\nRarity: " + item["rarity"] + "\nValue: " + item["value"] + "\nWeight: " + item["weight"] + "\n\n" + item["description"] + "\n\n"
            self.infoQuantity = "Quantity: " + str(item["quantity"])

        print(item)

    def refresh_item_quantity(self, item):
        # Exclusively for refreshing item quantity in the case of changes.
        
        self.infoQuantity = "Quantity: " + str(item["quantity"])

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
        usedQuant = 1
        if self.quantity >= 1:
                usedQuant=self.quantity
        item = Item(
            name=self.name,
            itemID=self.nextCustomID,
            rarity=self.rarity,
            weight=self.weight,
            value=self.value,
            category=self.category,
            description=self.description,
            quantity=usedQuant,
            type = "basic"
        )
        self.nextCustomID = self.nextCustomID + 1
        print("Adding basic item")

        self.add_item_to_inv(title="BASIC", item=item)
        self.dialog_open = False
        self.name = ""
        self.rarity = ""
        self.weight = ""
        self.value = ""
        self.category = ""
        self.description = ""
        self.quantity = 1
    
    def create_consumable_item(self):
        usedQuant = 1
        if self.quantity >= 1:
                usedQuant=self.quantity
        item = Item(
            name=self.name,
            itemID=self.nextCustomID,
            rarity=self.rarity,
            weight=self.weight,
            value=self.value,
            category=self.category,
            description=self.description,
            quantity=usedQuant,
            type="consumable"
        )

        print("Adding consumable item")
        self.nextCustomID = self.nextCustomID + 1

        self.add_item_to_inv(title="CONSUMABLES", item=item)
        self.dialog_open = False
        self.name = ""
        self.rarity = ""
        self.weight = ""
        self.value = ""
        self.category = ""
        self.description = ""
        self.quantity = 1

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
        usedQuant = 1
        if self.quantity >= 1:
                usedQuant=self.quantity
        weapon = Weapon(
            name=self.name,
            itemID=self.nextCustomID,
            martial=self.martial,
            damage=self.damage,
            damageType=self.damageType,
            rarity=self.rarity,
            tags=self.tags,
            weight=self.weight,
            value=self.value,
            description=self.description,
            quantity=usedQuant,
            type="weapon"
        )
        self.nextCustomID = self.nextCustomID + 1

        self.add_item_to_inv(title="WEAPONS", item=weapon)
        self.dialog_open = False
        self.name = ""
        self.martial = ""
        self.damage = ""
        self.damageType = ""
        self.rarity = ""
        self.tags = ""
        self.weight = ""
        self.value = ""
        self.description = ""
        self.quantity = 1

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
        usedQuant = 1
        if self.quantity >= 1:
                usedQuant=self.quantity
        armor = Armor(
            name=self.name,
            itemID=self.nextCustomID,
            weightClass=self.weightClass,
            AC=self.AC,
            rarity=self.rarity,
            weight=self.weight,
            value=self.value,
            description=self.description,
            quantity=usedQuant,
            type="armor"
        )
        self.nextCustomID = self.nextCustomID + 1
        self.add_item_to_inv(title="ARMOR", item=armor)
        self.dialog_open = False
        self.name = ""
        self.weightClass = ""
        self.AC = ""
        self.rarity = ""
        self.weight = ""
        self.value = ""
        self.description = ""
        self.quantity = 1