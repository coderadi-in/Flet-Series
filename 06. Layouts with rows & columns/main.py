'''PyCOD3 | @py.cod3'''

# ? Importing libraries
import flet as ft

# ! The main function
def main(page: ft.Page):
    card = ft.Container(
        content=ft.Column([
            ft.Row([
                ft.Image(
                    src="img.png",
                    border_radius=50,
                    width=50,
                    height=50
                ),
                ft.Text(
                    value="Card title",
                    size=36
                )
            ]),

            ft.Text(
                value="Very few sedans generate as much heart beating and adrenaline as the BMW M5.",
                size=16
            ),

            ft.Row([
                ft.FilledButton("Follow"),
                ft.TextButton("Message")
            ], alignment=ft.MainAxisAlignment.END)
        ], spacing=10),
        padding=20,
        border_radius=20,
        bgcolor="#1A1A1D",
        width=300
    )

    page.add(card)

ft.app(main)