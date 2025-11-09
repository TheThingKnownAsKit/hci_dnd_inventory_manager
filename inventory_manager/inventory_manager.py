"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config


class State(rx.State):
    """The app state."""



###-------------------------###
### CHARACTER SHEET SECTION ###
###-------------------------###

def character_scheet():
    return rx.flex(
        rx.box("Character sheet", p=4, bg="red.200"),
        direction="column",
        flex=1,
    )

###-----------------###
### WEAPONS SECTION ###
###-----------------###

def weapons():
    return rx.box("Weapons", p=4, bg="green.200")

###---------------###
### ARMOR SECTION ###
###---------------###

def armor():
    return rx.box("Armor", p=4, bg="green.300")

###---------------------###
### CONSUMABLES SECTION ###
###---------------------###

def consumables():
    return rx.box("Consumables", p=4, bg="green.400")

###----------------###
### BASICS SECTION ###
###----------------###

def basics():
    return rx.box("Basics", p=4, bg="blue.200")

###---------------------###
### INFORMATION SECTION ###
###---------------------###

def information():
    return rx.box("Information", p=4, bg="blue.300")



def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.flex(
        character_scheet(),
        rx.flex(
            weapons(),
            armor(),
            consumables(),
            direction="column",
            flex=1,
        ),
        rx.flex(
            basics(),
            information(),
            direction="column",
            flex=1,
        ),
        direction="row",
        gap=2,
        height="100vh",
    )


app = rx.App()
app.add_page(index)
