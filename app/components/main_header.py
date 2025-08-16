import reflex as rx

from app.states.states import State


def main_header() -> rx.Component:
    tabs = State.tabs
    return rx.el.header(
        rx.el.div(
            # Tab group (wraps + scrolls on small screens)
            rx.el.div(
                rx.el.img(
                    src="/android-chrome-192x192.png",
                    class_name="h-6 w-6 mr-4 flex-shrink-0 max-md:hidden",
                    on_click=rx.redirect('/')
                ),
                rx.foreach(
                    tabs,
                    lambda tab: rx.el.button(
                        tab,
                        on_click=State.set_active_main_tab(tab),
                        class_name=rx.cond(
                            State.active_tab == tab,
                            "px-1 py-2 text-sm font-medium text-white border-b-2 border-green-500",
                            "px-1 py-2 text-sm font-medium text-gray-400 hover:text-white hover:border-b-2 hover:border-gray-500",
                        ),
                    ),
                ),
                class_name="flex flex-wrap items-center space-x-1 overflow-x-auto whitespace-nowrap py-2",  # wrap + scroll + padding :contentReference[oaicite:7]{index=7} :contentReference[oaicite:8]{index=8} :contentReference[oaicite:9]{index=9}
            ),
            # Control group (wraps on mobile, resets margin at md)
            rx.el.div(
                rx.el.div(
                    rx.cond(
                        State.login,
                        rx.el.div(
                            rx.el.select(
                                rx.el.option("Basic", value="basic"),
                                rx.el.option("Advanced", value="advanced"),
                                default_value=State.default_version,
                                class_name="bg-gray-700 text-white text-xs rounded border-0 focus:ring-0 mr-3 py-1",
                                on_change=State.set_version,
                            ),
                            rx.el.button(
                                "Logout",
                                on_click=State.logout(),
                                class_name="bg-red-500 hover:bg-red-600 text-white text-xs font-bold py-1 px-4 rounded"
                            ),
                        ),
                        rx.el.div(
                            rx.el.button(
                                "Sign up",
                                on_click=rx.redirect("/sign-up"),
                                class_name="bg-blue-500 hover:bg-blue-600 text-white text-xs font-bold py-1 px-4 rounded mr-2"
                            ),
                            rx.el.button(
                                "Login",
                                on_click=rx.redirect("/login"),
                                class_name="bg-green-500 hover:bg-green-600 text-white text-xs font-bold py-1 px-4 rounded mr-2"
                            )
                        )


                    ),



                    class_name="flex items-center",
                ),
                class_name="flex flex-wrap items-center space-x-4 mt-2 md:mt-0 max-md:hidden",  # wrap + reset margin :contentReference[oaicite:10]{index=10}
            ),
            # Outer wrapper: stack on mobile, row at md and above
            class_name="flex flex-col md:flex-row justify-between items-center w-full",  # responsive direction :contentReference[oaicite:11]{index=11}
        ),
        class_name="bg-gray-900 text-gray-300 px-4 py-2 border-b border-gray-700",  # container styling :contentReference[oaicite:12]{index=12}
    )
