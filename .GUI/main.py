import sys
import os

# Add parent directory to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from flet import *
import flet as ft
from models.locals.Luna import luna


def main(page: Page):
    page.title = "Luna"
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.bgcolor = colors.WHITE

    page.add(
        Column(
            alignment="center",
            horizontal_alignment="center",
            controls=[
                ft.Lottie(
                    src="https://lottie.host/a0c4713d-454b-42c6-9a56-b15eb4fd458c/cmGrRQ6jCu.json",
                    animate=True,
                    repeat=True,
                )
            ]
        )
    )
    luna(None)


if __name__ == "__main__":
    app(target=main)
