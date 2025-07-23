# Layouts with container

[`Container`](https://flet.dev/docs/controls/container) allows to decorate a [control](https://flet.dev/docs/controls) with background color and border and position it with padding, margin and alignment.

## Syntax

```python
ft.Container(
    content=ft.Text("Styled text.", color="#000000"),
    width=300,
    height=150,
    alignment=ft.alignment.center,
    padding=10,
    border_radius=10,
    bgcolor="#FFCCCC"
)
```
## Arguments

Argument | Description
-|-
`content` | The [control](https://flet.dev/docs/controls) to be styled.
`width` | Width of container.
`height` | Height of container.
`alignment` | Alignment of [control](https://flet.dev/docs/controls) in the container.
`padding` | Padding in container.
`border_radius` | Corner smoothing.
`bgcolor` | Background color of container.
`ink` | Adds click effect.
`on_click` | Runs a command after click.
`gradient` | Adds gradient color.