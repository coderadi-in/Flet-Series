'''PyCOD3 | @py.cod3'''

# ? Importing libraries
import flet as ft

btns = [
    ['1', '2', '3', '+'],
    ['4', '5', '6', '-'],
    ['7', '8', '9', '*'],
    ['.', '0', '=', '/']
]

# ! The main function
def main(page: ft.Page):
    page.title = "Simple calculator"
    page.bgcolor = "#1A1A1D"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # & page elements
    display = ft.TextField(hint_text="Calculator")
    keyboard = ft.Column(spacing=10)

    # * function to clear display
    def clear(e):
        display.value = ""
        display.update()

    # * function to handle key presses
    def on_click(e):
        if e.control.text == '=':
            try:
                display.value = str(eval(display.value))

            except:
                display.value = "Error"

        else: display.value += e.control.text
        display.update()

    # & Buttons
    for row in btns:
        keyline = ft.Row(spacing=10, expand=True)
        for btn in row:
            keyline.controls.append(
                ft.FloatingActionButton(
                    btn,
                    foreground_color="#FFFFFF",
                    bgcolor="#4C8EFF",
                    on_click=on_click,
                    expand=True
                )
            )
        keyboard.controls.append(keyline)

    keyboard.controls.append(ft.Row([
        ft.FloatingActionButton(
            "C", on_click=clear,
            bgcolor="#4C8EFF",
            foreground_color="#FFFFFF",
            expand=True
        )
    ], expand=True))

    page.add(
        ft.Column([
            display,
            keyboard
        ], spacing=10)
    )

# ! Run the app
ft.app(main)