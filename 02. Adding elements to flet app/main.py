'''PyCOD3 | @py.cod3'''

# | pip install flet

# ? Importing libraries
import flet as ft

# ! The main function
def main(page: ft.Page):
    page.title = "02. Adding elements in flet app"

    # & adding elements
    txt = ft.Text(
        "Hello, World!",
        size=32,
        color="#FFFDD0"
    )

    inp = ft.TextField(
        label="Your name",
        hint_text="Enter your name",
        width=300
    )

    def func(e):
        print(inp.value)
        inp.value = ""
        txt.value = "Hi"
        page.update()

    btn = ft.ElevatedButton(
        text="Click Me!",
        on_click=func
    )

    page.add(txt, inp, btn)

# ! Run the app
ft.app(main)