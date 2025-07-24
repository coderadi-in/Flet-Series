# Flet card component &bull; PyCOD3

## Overivew
This Python script creates a simple card component using the Flet framework. The card displays an image, title, description, and action buttons in a visually appealing layout.

## Installation

```bash
pip install flet
```

## Code structure

### 1. Import

```python
import flet as ft
```

### 2. Main function

```python
def main(page: ft.Page):
```

### 3. Card component

```python
card = ft.Container(
    content=ft.Column([...]),
    padding=20,
    border_radius=20,
    bgcolor="#1A1A1D",
    width=300
)
```

Property | Value | Description
-|-|-
padding | 20 | Inner spacing
border_radius | 20 | Rounded corners
bgcolor | "#1A1A1D" | Dard background color
width | 300 | Fixed width in pixels

### 4. Card sections

### Header row

```python
ft.Row([
    ft.Image(src="img.png", border_radius=50, width=50, height=50),
    ft.Text(value="Card title", size=36)
])
```

### Description

```python
ft.Text(
    value="Very few sedans generate...",
    size=16
)
```

### Action buttons

```python
ft.Row([
    ft.FilledButton("Follow"),
    ft.TextButton("Message")
], alignment=ft.MainAxisAlignment.END)
```

### Final setup

```python
page.add(card)
ft.app(main)
```

## Visual representation

![Card screenshot](image.png)

## Notes

- Requires `img.png` in same directory
- All measurements in pixels
- Color values in hex format

## Customization tips

- Change bgcolor for different backgrounds
- Modify border_radius for corner styling
- Adjust width for responsive layouts
- Add more widgets to the Column or Row