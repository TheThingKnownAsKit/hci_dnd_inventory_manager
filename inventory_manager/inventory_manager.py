"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config


class State(rx.State):
    """The app state."""

###-------------------------###
### CHARACTER SHEET SECTION ###
###-------------------------###

def character_scheet():
    pass

###-----------------###
### WEAPONS SECTION ###
###-----------------###

def weapons():
    pass

###---------------###
### ARMOR SECTION ###
###---------------###

def armor():
    pass

###---------------------###
### CONSUMABLES SECTION ###
###---------------------###

def consumables():
    pass

###----------------###
### BASICS SECTION ###
###----------------###

def basics():
    pass

###---------------------###
### INFORMATION SECTION ###
###---------------------###

def information():
    pass



def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Welcome to Reflex!", size="9"),
            rx.text(
                "Get started by editing ",
                rx.code(f"{config.app_name}/{config.app_name}.py"),
                size="5",
            ),
            rx.link(
                rx.button("Check out our docs!"),
                href="https://reflex.dev/docs/getting-started/introduction/",
                is_external=True,
            ),
            spacing="5",
            align="start",
            justify="center",
            min_height="85vh",
        ),
    )


app = rx.App()
app.add_page(index)
