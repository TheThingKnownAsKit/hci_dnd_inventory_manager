import reflex as rx
from inventory_manager.components import character_sheet, inventory_container, information_container


def index() -> rx.Component:
    return rx.el.main(
        rx.el.div(
            rx.el.div(character_sheet(), class_name="w-1/3 p-2"),
            rx.el.div(
                inventory_container("WEAPONS", "bg-blue-400"),
                inventory_container("ARMOR", "bg-red-400"),
                inventory_container("CONSUMABLES", "bg-green-400"),
                class_name="w-1/3 p-2 flex flex-col gap-4",
            ),
            rx.el.div(
                inventory_container("BASIC", "bg-orange-400"),
                information_container(),
                class_name="w-1/3 p-2 flex flex-col gap-4",
            ),
            class_name="flex flex-row w-full h-screen",
        ),
        class_name="bg-yellow-100 font-['Inter']",
    )


app = rx.App(
    theme=rx.theme(appearance="light"),
    head_components=[
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(rel="preconnect", href="https://fonts.gstatic.com", cross_origin=""),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap",
            rel="stylesheet",
        ),
    ],
)
app.add_page(index)