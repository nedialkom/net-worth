import reflex as rx
from app.states.states import State

def main_page() -> rx.Component:
        return rx.cond(
            State.login,
            rx.el.main("Main Content individual page"),
            rx.el.main("Welcome on our page, please login")
        )