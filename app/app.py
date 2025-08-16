import reflex as rx
from . import navigation
from . import pages


app = rx.App()
app.add_page(pages.index, route=navigation.routes.HOME_ROUTE)
app.add_page(pages.sign_up, route=navigation.routes.SIGN_UP_ROUTE)
app.add_page(pages.login, route=navigation.routes.LOGIN_ROUTE)
