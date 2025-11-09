import reflex as rx
from inventory_manager.state import AppState, Stat, AddCustomItemState, AddCustomWeaponState, AddCustomArmorState


def _container_header(title: str, color: str) -> rx.Component:
    return rx.el.div(
        rx.el.p(title, class_name="font-bold text-white text-lg tracking-wide"),
        class_name=f"p-2 rounded-t-lg border-b-2 border-black {color}",
    )


data_map = {
    "WEAPONS": AppState.weaponData,
    "ARMOR": AppState.armorData,
    "CONSUMABLES": AppState.consumableData,
    "BASIC": AppState.basicData,
}

def get_current_inv(): return {
    "WEAPONS": AppState.weaponInv,
    "ARMOR": AppState.armorInv,
    "CONSUMABLES": AppState.consumableInv,
    "BASIC": AppState.basicInv,
}
custom_state_map = {
    "WEAPONS": AddCustomWeaponState,
    "ARMOR": AddCustomArmorState,
    "CONSUMABLES": AddCustomItemState,
    "BASIC": AddCustomItemState,
}

def _custom_item_creation(title: str):
    pass


# This is where the Add Item button goes
def _item_container_subheader(title: str) -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(  # This is the add item button
            rx.el.button(
                rx.icon(tag="circle_plus", class_name="text-green-600 mr-2"),
                "Add Item",
                class_name="flex items-center text-sm font-semibold text-gray-700",
            ),
            class_name="p-2 border-b-2 border-black bg-gray-200",
        ),
        rx.dialog.content(  # This is the add items dialog popup
            rx.dialog.title(f"Add {title} Item"),
            rx.dialog.root( # This is the add custom items dialog popup
                rx.dialog.trigger(
                    rx.el.button(f"Add Custom {title}",
                        class_name="flex items-center text-sm font-semibold text-gray-700",
                    ),
                    class_name="p-2 border-b-2 border-black bg-gray-200",
                ),
                rx.dialog.content(
                    f"Add Custom {title}",
                    rx.el.div(
                        rx.cond(    # Add a custom weapon
                            (title == "WEAPONS"),
                            rx.form(
                                rx.el.label("Name", class_name="text-sm font-semibold"),
                                rx.el.input(
                                    on_change=AddCustomWeaponState.set_name,  # type: ignore
                                    class_name="w-full p-2 border-2 border-black bg-gray-200",
                                ),
                                rx.el.label("Martial? True or False", class_name="text-sm font-semibold"),
                                rx.el.input(
                                    on_change=AddCustomWeaponState.set_martial,  # type: ignore
                                    class_name="w-full p-2 border-2 border-black bg-gray-200",
                                ),
                                rx.el.label("Damage", class_name="text-sm font-semibold"),
                                rx.el.input(
                                    on_change=AddCustomWeaponState.set_damage,  # type: ignore
                                    class_name="w-full p-2 border-2 border-black bg-gray-200",
                                ),
                                rx.el.label("Damage Type", class_name="text-sm font-semibold"),
                                rx.el.input(
                                    on_change=AddCustomWeaponState.set_damageType,  # type: ignore
                                    class_name="w-full p-2 border-2 border-black bg-gray-200",
                                ),
                                rx.el.label("Rarity", class_name="text-sm font-semibold"),
                                rx.el.input(
                                    on_change=AddCustomWeaponState.set_rarity,  # type: ignore
                                    class_name="w-full p-2 border-2 border-black bg-gray-200",
                                ),
                                rx.el.label("Tags", class_name="text-sm font-semibold"),
                                rx.el.input(
                                    on_change=AddCustomWeaponState.set_tags,  # type: ignore
                                    class_name="w-full p-2 border-2 border-black bg-gray-200",
                                ),
                                rx.el.label("Weight", class_name="text-sm font-semibold"),
                                rx.el.input(
                                    on_change=AddCustomWeaponState.set_weight,  # type: ignore
                                    class_name="w-full p-2 border-2 border-black bg-gray-200",
                                ),
                                rx.el.label("Value", class_name="text-sm font-semibold"),
                                rx.el.input(
                                    on_change=AddCustomWeaponState.set_value,  # type: ignore
                                    class_name="w-full p-2 border-2 border-black bg-gray-200",
                                ),
                                rx.el.label("Description", class_name="text-sm font-semibold"),
                                rx.el.input(
                                    on_change=AddCustomWeaponState.set_description,  # type: ignore
                                    class_name="w-full p-2 border-2 border-black bg-gray-200",
                                ),
                                rx.el.div(  # wrap Quantity label + input in a column
                                    rx.el.label("Quantity", class_name="text-sm font-semibold"),
                                    rx.el.input(
                                        default_value=1,  # type: ignore
                                        on_change=AddCustomWeaponState.set_quantity,  # type: ignore
                                        class_name="w-16 p-2 border-2 border-black bg-gray-200 text-center",
                                        type="number",
                                    ),
                                    class_name="flex flex-col mb-2",  # flex-col to stack vertically
                                ),
                                rx.button("Add Weapon", type="submit"),
                                on_submit=lambda: AddCustomWeaponState.create_weapon,
                                class_name="flex-grow",
                            ),
                        ),
                        rx.cond(    # Add a custom armor
                            (title == "ARMOR"),
                            rx.form(
                                rx.el.label("Name", class_name="text-sm font-semibold"),
                                rx.el.input(
                                    on_change=AddCustomArmorState.set_name,  # type: ignore
                                    class_name="w-full p-2 border-2 border-black bg-gray-200",
                                ),
                                rx.el.label("Weight Class", class_name="text-sm font-semibold"),
                                rx.el.input(
                                    on_change=AddCustomArmorState.set_weightClass,  # type: ignore
                                    class_name="w-full p-2 border-2 border-black bg-gray-200",
                                ),
                                rx.el.label("AC", class_name="text-sm font-semibold"),
                                rx.el.input(
                                    on_change=AddCustomArmorState.set_AC,  # type: ignore
                                    class_name="w-full p-2 border-2 border-black bg-gray-200",
                                ),
                                rx.el.label("Rarity", class_name="text-sm font-semibold"),
                                rx.el.input(
                                    on_change=AddCustomArmorState.set_rarity,  # type: ignore
                                    class_name="w-full p-2 border-2 border-black bg-gray-200",
                                ),
                                rx.el.label("Weight", class_name="text-sm font-semibold"),
                                rx.el.input(
                                    on_change=AddCustomArmorState.set_weight,  # type: ignore
                                    class_name="w-full p-2 border-2 border-black bg-gray-200",
                                ),
                                rx.el.label("Value", class_name="text-sm font-semibold"),
                                rx.el.input(
                                    on_change=AddCustomArmorState.set_value,  # type: ignore
                                    class_name="w-full p-2 border-2 border-black bg-gray-200",
                                ),
                                rx.el.label("Description", class_name="text-sm font-semibold"),
                                rx.el.input(
                                    on_change=AddCustomArmorState.set_description,  # type: ignore
                                    class_name="w-full p-2 border-2 border-black bg-gray-200",
                                ),
                                rx.el.div(  # wrap Quantity label + input in a column
                                    rx.el.label("Quantity", class_name="text-sm font-semibold"),
                                    rx.el.input(
                                        default_value=1,  # type: ignore
                                        on_change=AddCustomArmorState.set_quantity,  # type: ignore
                                        class_name="w-16 p-2 border-2 border-black bg-gray-200 text-center",
                                        type="number",
                                    ),
                                    class_name="flex flex-col mb-2",  # flex-col to stack vertically
                                ),
                                rx.button("Add Armor", type="submit"),
                                on_submit=lambda: AddCustomArmorState.create_armor,
                                class_name="flex-grow",
                            ),
                        ),
                        rx.cond(    # Add a custom consumable or basic item
                            (title == "BASIC" or title == "CONSUMABLES"),
                            rx.form(
                                rx.el.label("Name", class_name="text-sm font-semibold"),
                                rx.el.input(
                                    on_change=AddCustomItemState.set_name,  # type: ignore
                                    class_name="w-full p-2 border-2 border-black bg-gray-200",
                                ),
                                rx.el.label("Rarity", class_name="text-sm font-semibold"),
                                rx.el.input(
                                    on_change=AddCustomItemState.set_rarity,  # type: ignore
                                    class_name="w-full p-2 border-2 border-black bg-gray-200",
                                ),
                                rx.el.label("Weight", class_name="text-sm font-semibold"),
                                rx.el.input(
                                    on_change=AddCustomItemState.set_weight,  # type: ignore
                                    class_name="w-full p-2 border-2 border-black bg-gray-200",
                                ),
                                rx.el.label("Value", class_name="text-sm font-semibold"),
                                rx.el.input(
                                    on_change=AddCustomItemState.set_value,  # type: ignore
                                    class_name="w-full p-2 border-2 border-black bg-gray-200",
                                ),
                                rx.el.label("Category", class_name="text-sm font-semibold"),
                                rx.el.input(
                                    on_change=AddCustomItemState.set_category,  # type: ignore
                                    class_name="w-full p-2 border-2 border-black bg-gray-200",
                                ),
                                rx.el.label("Description", class_name="text-sm font-semibold"),
                                rx.el.input(
                                    on_change=AddCustomItemState.set_description,  # type: ignore
                                    class_name="w-full p-2 border-2 border-black bg-gray-200",
                                ),
                                rx.el.div(  # wrap Quantity label + input in a column
                                    rx.el.label("Quantity", class_name="text-sm font-semibold"),
                                    rx.el.input(
                                        default_value=1,  # type: ignore
                                        on_change=AddCustomItemState.set_quantity,  # type: ignore
                                        class_name="w-16 p-2 border-2 border-black bg-gray-200 text-center",
                                        type="number",
                                    ),
                                    class_name="flex flex-col mb-2",  # flex-col to stack vertically
                                ),
                                rx.button("Add Item", type="submit"),
                                on_submit=(
                                    AddCustomItemState.create_basic_item
                                    if title == "BASIC"
                                    else AddCustomItemState.create_consumable_item
                                ), # type: ignore
                                class_name="flex-grow",
                            ),
                        ),
                    ),
                ),
                open=AppState.dialog_open,
                on_open_change=AppState.set_dialog_open, # type: ignore
            ),
            rx.scroll_area( # This is the list of premade items to add
                rx.foreach(
                    data_map[title],
                    lambda item: rx.el.div(
                        rx.el.button(
                            rx.text(item["name"]),
                            class_name="font-bold text-black text-sm tracking-wide",
                            on_click=lambda: AppState.add_item_to_inv(title, item), # type: ignore
                        ),
                        class_name="p-2 border-b border-gray-300"
                    )
                ),
                class_name="flex-grow p-4 bg-yellow-50"
            ),
        ),
    )


def inventory_container(title: str, color: str) -> rx.Component:
    return rx.el.div(
        _container_header(title, color),
        _item_container_subheader(title=title),
        rx.scroll_area( # This is the list of premade items to add
            rx.el.div(    
                rx.foreach(
                    get_current_inv()[title],
                    lambda item: rx.el.div(
                        rx.el.button(
                            rx.box(width="50px", height="50px", aspect_ratio=1, background="center/cover url('/potion.jpg')"),
                            rx.text(item["name"],
                                    style={
                                        "width": "100%",
                                        "fontSize": "calc(0.2 * 50px)",
                                        "whiteSpace": "normal",
                                        "overflow": "visible",
                                        "textAlign": "center",
                                        "wordBreak": "break-word"
                                    }),
                            class_name="flex flex-col justify-end items-center flex-grow p-1 bg-gray-300 border-2 border-black rounded font-bold text-black tracking-wide",
                            on_click=lambda: AppState.add_item_to_inv(title, item), # type: ignore
                        ),
                        class_name="p-2 border-b border-gray-300"
                    )
                    
                ),
                class_name="flex flex-wrap gap-2 justify-start items-start p-4 bg-yellow-50"
            ),
             class_name="flex-grow p-4 bg-yellow-50",

        ),
        style={
            "minHeight": "150px",
            "maxHeight": "500px",
            "display": "flex",
            "flexDirection": "column",
        },
    class_name="flex flex-col border-2 border-black rounded-lg w-full h-full shadow-md",
    )


def stat_display(stat: Stat) -> rx.Component:
    color_map = {
        "red": "bg-red-500",
        "orange": "bg-orange-500",
        "yellow": "bg-yellow-500",
        "green": "bg-green-500",
        "blue": "bg-blue-500",
        "purple": "bg-purple-500",
    }
    color_map_var = rx.Var.create(color_map)
    return rx.el.div(
        rx.el.div(
            stat["name"],
            class_name="absolute top-0 w-full text-center text-base font-semibold bg-gray-200 border-b border-black py-0.5",
        ),
        rx.el.div(
            stat["value"],
            class_name="absolute bottom-2 w-full text-center text-xl font-bold text-white",
        ),
        class_name=f"relative w-28 h-24 {color_map_var[stat['color']]} text-black",
        style={
            "clip_path": "polygon(25% 0%, 75% 0%, 100% 50%, 75% 100%, 25% 100%, 0% 50%)"
        },
    )


def character_sheet() -> rx.Component:
    return rx.el.div(
        _container_header("CHARACTER SHEET", "bg-purple-500"),
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.label("Name", class_name="text-sm font-semibold"),
                    rx.el.input(
                        default_value=AppState.character_name,
                        on_change=AppState.set_character_name, # type: ignore
                        class_name="w-full p-2 border-2 border-black bg-gray-200",
                    ),
                    class_name="flex-grow",
                ),
                rx.el.div(
                    rx.el.label("Level", class_name="text-sm font-semibold"),
                    rx.el.input(
                        default_value=AppState.level.to_string(), # type: ignore
                        on_change=AppState.set_level, # type: ignore
                        class_name="w-16 p-2 border-2 border-black bg-gray-200 text-center",
                        type="number",
                    ),
                ),
                class_name="flex gap-4 p-4 items-end",
            ),
            rx.el.div(
                rx.el.label("Race", class_name="text-sm font-semibold"),
                rx.el.input(
                    default_value=AppState.character_race,
                    on_change=AppState.set_character_race, # type: ignore
                    class_name="w-full p-2 border-2 border-black bg-gray-200",
                ),
                class_name="px-4 pb-4",
            ),
            rx.el.div(
                rx.foreach(AppState.stats, stat_display),
                class_name="grid grid-cols-3 gap-y-4 gap-x-2 p-4 justify-items-center",
            ),
            class_name="bg-yellow-50 flex-grow",
        ),
        class_name="flex flex-col border-2 border-black rounded-lg shadow-md h-full",
    )


def information_container() -> rx.Component:
    return rx.el.div(
        _container_header("INFORMATION", "bg-yellow-400"),
        rx.el.div(class_name="flex-grow p-4 bg-yellow-50"),
        class_name="flex flex-col border-2 border-black rounded-lg w-full h-full shadow-md",
    )