'''PyCOD3 | @py.cod3'''

# ? Importing libraries
import flet as ft

# ! The main function
def main(page: ft.Page):
    page.title = "Layouts with container"

    container = ft.Container(
        content=ft.Text(
            value="Content",
            color="#000000"
        ),
        padding=10,
        border_radius=10,
        ink=True,
        width=300,
        height=100,
        alignment=ft.alignment.center,
        on_click=lambda e: None,
        gradient=ft.LinearGradient([
            "#FFCCCC",
            "#CCFFCC",
            "#CCCCFF",
        ])
    )

    page.add(container)

# ! Run the app
ft.app(main)