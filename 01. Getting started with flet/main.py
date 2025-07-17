'''PyCOD3 | @py.cod3'''

# | pip install flet

# ? Importing libraries
import flet as ft

# ! The main function
def main(page: ft.Page):
    page.title = "01. Getting started with Flet"

    # & adding elements

    page.update()

# ! Run the app
ft.app(main)