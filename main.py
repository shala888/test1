import flet as ft 
from datetime import datetime

def main(page: ft.Page):
    page.title = 'Мое первое приложение!'
    page.theme_mode = ft.ThemeMode.DARK
    page.window_width = 450 

   
    history_data = []

    text_hello = ft.Text(value='Введите имя и нажмите send')
    
    history_column = ft.Column()

    def update_history_view(filter_type=None):
        """Функция для обновления отображения списка на экране"""
        history_column.controls.clear()
        
        display_list = history_data[-5:]

        for item in display_list:
            hour = item['time'].hour
            if filter_type == "morning" and hour >= 12:
                continue
            if filter_type == "evening" and hour < 12:
                continue
            
           
            history_column.controls.append(ft.Text(f"{item['text']} ({item['time'].strftime('%H:%M:%S')})"))
        
        page.update()

    def on_click_func(_):
        name = name_input.value
        if name:
            msg = f'Hello {name}'
            text_hello.value = msg
            text_hello.color = None
            
            
            history_data.append({
                "text": msg,
                "time": datetime.now()
            })
            
            name_input.value = "" 
            update_history_view() 
        else: 
            text_hello.color = ft.Colors.RED
            text_hello.value = 'Введите корректное имя!'
        
        page.update()

    name_input = ft.TextField(label='Введите имя', expand=True, on_submit=on_click_func)
    elevated_button = ft.ElevatedButton('send', icon=ft.Icons.SEND, on_click=on_click_func)

    filter_buttons = ft.Row([
        ft.OutlinedButton("Утро (до 12:00)", on_click=lambda _: update_history_view("morning")),
        ft.OutlinedButton("Вечер (после 12:00)", on_click=lambda _: update_history_view("evening")),
        ft.TextButton("Все", on_click=lambda _: update_history_view())
    ])

    def edit_theme(_):
        page.theme_mode = ft.ThemeMode.LIGHT if page.theme_mode == ft.ThemeMode.DARK else ft.ThemeMode.DARK
        page.update()

    theme_button = ft.IconButton(icon=ft.Icons.BRIGHTNESS_6, on_click=edit_theme)

    page.add(
        ft.Row([text_hello, theme_button], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
        ft.Row([name_input, elevated_button]),
        ft.Divider(),
        ft.Text("История (последние 5):", weight=ft.FontWeight.BOLD),
        filter_buttons,
        history_column
    )

ft.app(main)