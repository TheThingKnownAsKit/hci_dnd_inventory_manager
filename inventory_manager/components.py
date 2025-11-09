import reflex as rx
from inventory_manager.state import AppState, Stat


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


# This is where the Add Item button goes
def _item_container_subheader(title: str) -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.el.button(
                rx.icon(tag="circle_plus", class_name="text-green-600 mr-2"),
                "Add Item",
                class_name="flex items-center text-sm font-semibold text-gray-700",
            ),
            class_name="p-2 border-b-2 border-black bg-gray-200",
        ),
        rx.dialog.content(
            rx.dialog.title(f"Add {title} Item"),
            rx.dialog.root(         # This is where custom items are
                rx.dialog.trigger(
                    rx.el.button(f"Add Custom {title}",
                        class_name="flex items-center text-sm font-semibold text-gray-700",
                    ),
                    class_name="p-2 border-b-2 border-black bg-gray-200",
                ),
                rx.dialog.content(f"Add Custom {title}"),
            ),
            rx.scroll_area(
                rx.foreach(
                    data_map[title],  # Your state list here
                    lambda item: rx.el.div(
                        rx.text(item["name"], class_name="font-bold text-black text-sm tracking-wide"),
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
        rx.el.div(class_name="flex-grow p-4 bg-yellow-50"),
        class_name="flex flex-col border-2 border-black rounded-lg w-full h-full shadow-md",
    )


def character_sheet() -> rx.Component:
    stats = AppState.stats

    def stat_div(stat: Stat) -> rx.Component:
        return rx.el.div(
            rx.el.div(
                stat["name"],
                class_name="absolute top-0 w-full text-center text-base font-semibold bg-gray-200 border-b border-black py-0.5",
            ),
            rx.el.input(
                value=stat["value"],
                on_change=lambda value, stat_name=stat["name"]: AppState.update_stat(stat_name, value),
                class_name="absolute bottom-2 w-full text-center text-xl font-bold text-white bg-transparent border-none focus:outline-none",
                type="number",
            ),
            class_name=f"relative w-28 h-24 {stat['bg_class']} text-black",
            style={
                "clip_path": "polygon(25% 0%, 75% 0%, 100% 50%, 75% 100%, 25% 100%, 0% 50%)"
            },
        )
    
    return rx.el.div(
        _container_header("CHARACTER SHEET", "bg-purple-500"),
        rx.el.div(
            
            # --- Name / Level ---
            rx.el.div(
                rx.el.div(
                    rx.el.label("Name", class_name="text-base font-semibold"),
                    rx.el.input(
                        default_value=AppState.character_name,
                        on_change=AppState.set_character_name,
                        class_name="w-full p-2 border-2 border-black bg-gray-200",
                    ),
                    class_name="flex flex-col flex-[5]",
                ),
                rx.el.div(
                    rx.el.label("Level", class_name="text-base font-semibold self-start"),
                    rx.el.input(
                        default_value=AppState.level.to_string(),
                        on_change=AppState.set_level,
                        class_name="w-full p-2 border-2 border-black bg-gray-200 text-center",
                        type="number",
                    ),
                    class_name="flex flex-col flex-[1] items-end",
                ),
                class_name="flex gap-x-4 gap-y-2 p-4 items-end",
            ),

            # --- Class / Subclass ---
            rx.el.div(
                rx.el.div(
                    rx.el.label("Class", class_name="text-base font-semibold"),
                    rx.el.input(
                        default_value=AppState.character_class,
                        on_change=AppState.set_character_class,
                        class_name="w-full p-2 border-2 border-black bg-gray-200",
                    )
                ),
                rx.el.div(
                    rx.el.label("Subclass", class_name="text-base font-semibold"),
                    rx.el.input(
                        default_value=AppState.character_subclass,
                        on_change=AppState.set_character_subclass,
                        class_name="w-full p-2 border-2 border-black bg-gray-200",
                    ),
                ),
                class_name="flex gap-x-4 gap-y-2 p-4 items-end",
            ),

            # --- Race / Subrace ---
            rx.el.div(
                rx.el.div(
                    rx.el.label("Race", class_name="text-base font-semibold"),
                    rx.el.input(
                        default_value=AppState.character_race,
                        on_change=AppState.set_character_race,
                        class_name="w-full p-2 border-2 border-black bg-gray-200",
                    )
                ),
                rx.el.div(
                    rx.el.label("Subrace", class_name="text-base font-semibold"),
                    rx.el.input(
                        default_value=AppState.character_subrace,
                        on_change=AppState.set_character_subrace,
                        class_name="w-full p-2 border-2 border-black bg-gray-200",
                    ),
                ),
                class_name="flex gap-x-4 gap-y-2 p-4 items-end",
            ),

            # --- Stats Grid ---
            rx.el.div(
                rx.foreach(
                    stats,
                    lambda stat: stat_div(stat)
                ),
                class_name="grid grid-cols-3 gap-y-4 gap-x-2 p-4 justify-items-center",
            ),

            # --- Currency ---
            rx.el.div(
                rx.el.div(
                    rx.el.label("PP", class_name="text-base font-semibold self-start"),
                    rx.el.input(
                        default_value=AppState.character_pp.to_string(),
                        on_change=AppState.set_character_pp,
                        class_name="w-full p-2 border-2 border-black bg-gray-200 text-center",
                        type="number",
                    ),
                    class_name="flex flex-col",
                ),
                rx.el.div(
                    rx.el.label("GP", class_name="text-base font-semibold self-start"),
                    rx.el.input(
                        default_value=AppState.character_gp.to_string(),
                        on_change=AppState.set_character_gp,
                        class_name="w-full p-2 border-2 border-black bg-gray-200 text-center",
                        type="number",
                    ),
                    class_name="flex flex-col",
                ),
                rx.el.div(
                    rx.el.label("EP", class_name="text-base font-semibold self-start"),
                    rx.el.input(
                        default_value=AppState.character_ep.to_string(),
                        on_change=AppState.set_character_ep,
                        class_name="w-full p-2 border-2 border-black bg-gray-200 text-center",
                        type="number",
                    ),
                    class_name="flex flex-col",
                ),
                rx.el.div(
                    rx.el.label("SP", class_name="text-base font-semibold self-start"),
                    rx.el.input(
                        default_value=AppState.character_sp.to_string(),
                        on_change=AppState.set_character_sp,
                        class_name="w-full p-2 border-2 border-black bg-gray-200 text-center",
                        type="number",
                    ),
                    class_name="flex flex-col",
                ),
                rx.el.div(
                    rx.el.label("CP", class_name="text-base font-semibold self-start"),
                    rx.el.input(
                        default_value=AppState.character_cp.to_string(),
                        on_change=AppState.set_character_cp,
                        class_name="w-full p-2 border-2 border-black bg-gray-200 text-center",
                        type="number",
                    ),
                    class_name="flex flex-col",
                ),
                class_name="grid grid-cols-5 gap-x-4 gap-y-2 p-4 items-end",
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