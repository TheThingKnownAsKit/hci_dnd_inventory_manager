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
        {"name": "Strength", "value": 10, "color": "red"},
        {"name": "Dexterity", "value": 12, "color": "orange"},
        {"name": "Constitution", "value": 14, "color": "yellow"},
        {"name": "Intelligence", "value": 8, "color": "green"},
        {"name": "Wisdom", "value": 15, "color": "blue"},
        {"name": "Charisma", "value": 16, "color": "purple"},
    ]