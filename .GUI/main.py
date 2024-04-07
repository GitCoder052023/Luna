from flet import *
import flet as ft
from models.locals.Luna import luna


def main(page: Page):
    page.title = "Luna"
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"

    def change_content(e):
        page.controls.clear()
        nav_dest = e.control.selected_index

        if nav_dest == 0:
            nav_content = Column(
                controls=[
                    IconButton(icon=icons.ARROW_FORWARD, icon_size=20, on_click=show_drawer),
                    Column(
                        alignment="center",
                        horizontal_alignment="center",
                        controls=[
                            Text("Hello Sir, How can I help you today?", size=45, width="bold"),
                            Container(padding=padding.only(top=35)),
                            IconButton(icon=icons.MIC_OUTLINED, icon_size=130,
                                       tooltip="Start Listening",
                                       on_click=luna)
                        ]
                    )
                ]
            )
            page.add(nav_content)

    def show_drawer(e):
        page.drawer.open = True
        page.drawer.update()

    page.drawer = ft.NavigationDrawer(
        controls=[
            ft.Container(height=12),
            ft.NavigationDrawerDestination(
                label="Home",
                icon=ft.icons.HOME,
                selected_icon_content=ft.Icon(ft.icons.HOME),
            ),
        ],
        on_change=change_content,
        selected_index=0
    )

    page.add(
        Column(
            controls=[
                IconButton(icon=icons.ARROW_FORWARD, icon_size=20, on_click=show_drawer),
                Column(
                    alignment="center",
                    horizontal_alignment="center",
                    controls=[
                        Text("Hello Sir, How can I help you today?", size=45, width="bold"),
                        Container(padding=padding.only(top=35)),
                        IconButton(icon=icons.MIC_OUTLINED, icon_size=130,
                                   tooltip="Start Listening",
                                   on_click=luna)
                    ]
                )
            ]
        )
    )



if __name__ == "__main__":
    app(target=main)
