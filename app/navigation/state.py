import reflex as rx

from . import routes


class NavState(rx.State):
    def to_home(self):
        """
        on_click event
        """
        return rx.redirect(routes.HOME_ROUTE)

    def to_login(self):
        return rx.redirect(routes.LOGIN_ROUTE)

    def to_sign_up(self):
        return rx.redirect(routes.SIGN_UP_ROUTE)