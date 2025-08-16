import reflex as rx
from app.states.states import State
from app.components.main_header import main_header
from app.components.main_page import main_page
from app.components.currency_page import currency_page
from app.navigation import routes


def index() -> rx.Component:
    """The main page component for the trading dashboard."""
    return rx.el.div(
        main_header(),
        rx.el.main(
            rx.match(
                State.active_tab,
                ("Main", main_page()),
                ("Currency", currency_page()),
                ("Tickers", rx.el.main("Tickers Content")), # refactor like above -> individual _page.py file
            ),
            class_name="grid grid-cols-1 lg:grid-cols-3 gap-4 p-4",
        ),
        class_name="min-h-screen bg-gray-900 text-gray-300 font-sans",
    )