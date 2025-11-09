import reflex as rx
from typing import TypedDict


class Stat(TypedDict):
    name: str
    value: int
    color: str


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