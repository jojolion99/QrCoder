# Переключение светлой/тёмной темы
def toggle_theme():
    global current_theme
    if current_theme == "light":
        customtkinter.set_appearance_mode("Dark")  # Включить тёмную тему
        current_theme = "dark"
        theme_btn.configure(text="Светлая тема" if current_language == "ru" else "Light Theme")
    else:
        customtkinter.set_appearance_mode("Light")  # Включить светлую тему
        current_theme = "light"
        theme_btn.configure(text="Тёмная тема" if current_language == "ru" else "Dark Theme")