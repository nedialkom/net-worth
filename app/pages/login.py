import reflex as rx
from app.components.main_header import main_header

def login() -> rx.Component:
    return rx.el.div(
            main_header(),
            rx.center(
                rx.card(
                    rx.vstack(
                        rx.hstack(
                            rx.image(
                                src="/android-chrome-192x192.png",
                                width="2.5em",
                                height="auto",
                                border_radius="25%",
                            ),
                            rx.heading(
                                "Sign in to your account",
                                size="6",
                                as_="h2",
                                text_align="left",
                                width="100%",
                            ),
                        ),

                        rx.flex(

                            rx.hstack(
                                rx.text(
                                    "New here?",
                                    size="3",
                                    text_align="left",
                                ),
                                rx.link("Sign up", href="/sign-up", size="3"),
                                spacing="2",
                                opacity="0.8",
                                width="100%",
                            ),
                            direction="column",
                            justify="start",
                            spacing="4",
                            width="100%",
                        ),
                        rx.vstack(
                            rx.text(
                                "Email address",
                                size="3",
                                weight="medium",
                                text_align="left",
                                width="100%",
                            ),
                            rx.input(
                                rx.input.slot(rx.icon("user")),
                                placeholder="user@reflex.dev",
                                type="email",
                                size="3",
                                width="100%",
                            ),
                            justify="start",
                            spacing="2",
                            width="100%",
                        ),
                        rx.vstack(
                            rx.hstack(
                                rx.text(
                                    "Password",
                                    size="3",
                                    weight="medium",
                                ),
                                rx.link(
                                    "Forgot password?",
                                    href="#",
                                    size="3",
                                ),
                                justify="between",
                                width="100%",
                            ),
                            rx.input(
                                rx.input.slot(rx.icon("lock")),
                                placeholder="Enter your password",
                                type="password",
                                size="3",
                                width="100%",
                            ),
                            spacing="2",
                            width="100%",
                        ),
                        rx.button("Sign in", size="3", width="100%"),
                        rx.hstack(
                            rx.divider(margin="0"),
                            rx.text(
                                "Or continue with",
                                white_space="nowrap",
                                weight="medium",
                            ),
                            rx.divider(margin="0"),
                            align="center",
                            width="100%",
                        ),
                        rx.button(
                            rx.icon(tag="github"),
                            "Sign in with Github",
                            variant="outline",
                            size="3",
                            width="100%",
                        ),
                        spacing="6",
                        width="100%",
                    ),
                    size="4",
                    max_width="28em",
                    width="100%",
                )
        )
    )