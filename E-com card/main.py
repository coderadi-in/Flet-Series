'''PyCOD3 | @_py.code'''

# ? Importing libraries
import flet as ft

# ! The main function
def main(page: ft.Page):
    page.title = "ECommerce product card"

    product = ft.Container(
        content=ft.Column([
            ft.Image(
                src="product.jpg",
                width=300, height=300
            ),
            ft.Text(
                value="BMW M5 CS", 
                size=32, color="#F3F4F6",
                width=300
            ),
            ft.Row([
                ft.Row([
                    ft.Icon(
                        name=ft.Icons.STAR,
                        color="#77FF77",
                        size=16
                    )  for _ in range(5)
                ]),
                ft.FloatingActionButton(
                    text="Buy now.",
                    icon=ft.Icons.MONEY
                )
            ], width=350, alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
        ]),
        width=350, border_radius=5,
        bgcolor="#1A1A1D",
        padding=25
    )

    page.add(product)

# ! Run the app
ft.app(main)