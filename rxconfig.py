import reflex as rx

config = rx.Config(
    app_name="inventory_manager",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)