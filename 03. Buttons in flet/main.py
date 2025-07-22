'''PyCOD3 | @py.cod3'''

# ? Importing libraries
import flet as ft

# ! The main function
def main(page: ft.Page):
    page.title = "Flet buttons"

    # & Simple button
    btn1 = ft.ElevatedButton(
        text="Simple Button",
        icon=ft.Icons.ADD,
        width=300
    )
    
    # & Filled button
    btn2 = ft.FilledButton(
        text="Filled Button",
        icon=ft.Icons.ADD,
        width=300
    )

    # & FilledTonal button
    btn3 = ft.FilledTonalButton(
        text="Filled Tonal Button",
        icon=ft.Icons.ADD,
        width=300
    )

    # & Outlined button
    btn4 = ft.OutlinedButton(
        text="Outlined Button",
        icon=ft.Icons.ADD,
        width=300
    )

    # & Text button
    btn5 = ft.TextButton(
        text="Filled Button",
        width=300
    )

    # & Icon button
    btn6 = ft.IconButton(
        icon=ft.Icons.OPEN_IN_BROWSER,
        width=300
    )

    page.add(
        btn1,
        btn2,
        btn3, 
        btn4,
        btn5,
        btn6
    )

    

# ! Run the app
ft.app(main)