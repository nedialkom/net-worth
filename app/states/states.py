import reflex as rx
from app.navigation import routes

class State(rx.State):
    """The app state."""
    active_tab: str = "Main"
    tabs: list[str] = ["Main"]
    version: str = "basic"
    default_version: str = "basic"
    login: bool = True

    @rx.event
    def set_active_main_tab(self, tab_name: str):
        self.active_tab = tab_name
        #rx.redirect(routes.HOME_ROUTE)

    @rx.event
    def set_version(self, version: str):
        if version == "basic":
            self.tabs = ["Main"]
            self.active_tab = "Main"
        elif version == "advanced":
            self.tabs = ["Main", "Currency", "Tickers",]
            self.active_tab = "Main"
        self.version = version

    def logout(self):
        self.login = False
        self.set_version("basic")
        rx.redirect(routes.HOME_ROUTE)
