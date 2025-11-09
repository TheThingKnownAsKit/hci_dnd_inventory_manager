import reflex as rx
from inventory_manager.state import AppState, Stat


def _container_header(title: str, color: str) -> rx.Component:
    return rx.el.div(
        rx.el.p(title, class_name="font-bold text-white text-lg tracking-wide"),
        class_name=f"p-2 rounded-t-lg border-b-2 border-black {color}",
    )


def _item_container_subheader() -> rx.Component:
    return rx.el.div(
        rx.el.button(
            rx.icon(tag="circle_plus", class_name="text-green-600 mr-2"),
            "Add Item",
            class_name="flex items-center text-sm font-semibold text-gray-700",
        ),
        class_name="p-2 border-b-2 border-black bg-gray-200",
    )


def inventory_container(title: str, color: str) -> rx.Component:
    return rx.el.div(
        _container_header(title, color),
        _item_container_subheader(),
        rx.el.div(class_name="flex-grow p-4 bg-yellow-50"),
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
                        on_change=AppState.set_character_name,
                        class_name="w-full p-2 border-2 border-black bg-gray-200",
                    ),
                    class_name="flex-grow",
                ),
                rx.el.div(
                    rx.el.label("Level", class_name="text-sm font-semibold"),
                    rx.el.input(
                        default_value=AppState.level.to_string(),
                        on_change=AppState.set_level,
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
                    on_change=AppState.set_character_race,
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