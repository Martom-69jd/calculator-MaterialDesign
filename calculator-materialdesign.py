import flet as ft

def main(page: ft.Page):

    page.title = "Material Calculator"
    page.theme_mode = ft.ThemeMode.DARK
    page.theme = ft.Theme(color_scheme_seed=ft.colors.ORANGE)
    page.window.width = 350
    page.window.height = 550
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    result_text = ft.Text(
        value="0", 
        size=45, 
        text_align=ft.TextAlign.RIGHT, 
        weight=ft.FontWeight.W_500
    )

    def button_click(e):
        data = e.control.data
        if data == "C":
            result_text.value = "0"
        elif data == "=":
            try:

                result_text.value = str(eval(result_text.value))
            except Exception:
                result_text.value = "Ошибка"
        else:
            if result_text.value == "0" or result_text.value == "Ошибка":
                result_text.value = str(data)
            else:
                result_text.value += str(data)
        page.update()

    def btn(text, bg_color=ft.colors.SURFACE_VARIANT, text_color=ft.colors.ON_SURFACE):
        return ft.ElevatedButton(
            text=text,
            data=text,
            on_click=button_click,
            width=65,
            height=65,
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=20), # Скругление в стиле MD3
                bgcolor=bg_color,
                color=text_color,
                padding=0,
            )
        )

    row1 = ft.Row(
        [btn("7"), btn("8"), btn("9"), btn("/", ft.colors.PRIMARY_CONTAINER)], 
        alignment=ft.MainAxisAlignment.CENTER
    )
    row2 = ft.Row(
        [btn("4"), btn("5"), btn("6"), btn("*", ft.colors.PRIMARY_CONTAINER)], 
        alignment=ft.MainAxisAlignment.CENTER
    )
    row3 = ft.Row(
        [btn("1"), btn("2"), btn("3"), btn("-", ft.colors.PRIMARY_CONTAINER)], 
        alignment=ft.MainAxisAlignment.CENTER
    )
    row4 = ft.Row(
        [btn("C", ft.colors.ERROR_CONTAINER), btn("0"), btn("="), btn("+", ft.colors.PRIMARY_CONTAINER)], 
        alignment=ft.MainAxisAlignment.CENTER
    )

    page.add(
        ft.Container(
            content=result_text,
            padding=ft.padding.only(right=20, bottom=20, top=20),
            alignment=ft.alignment.center_right
        ),
        row1, row2, row3, row4
    )


ft.app(target=main)
