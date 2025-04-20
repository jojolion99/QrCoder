# Функция переключения языка интерфейса (русский/английский)
def switch_language():
    global current_language
    if current_language == "ru":
        current_language = "en"  # Переключить на английский
        title_label.configure(text="Select QR code type:")
        generate_btn.configure(text="Create QR")
        lang_btn.configure(text="Switch to Russian")
        theme_btn.configure(text="Dark Theme" if current_theme == "light" else "Light Theme")
        about_btn.configure(text="About")

        # Заполнить плейсхолдеры на английском
        url_entry.configure(placeholder_text="Enter URL")
        ssid_entry.configure(placeholder_text="Network Name (SSID)")
        wifi_password_entry.configure(placeholder_text="Password")
        text_entry.configure(placeholder_text="Enter text")
        phone_entry.configure(placeholder_text="Enter phone number")
        email_entry.configure(placeholder_text="Enter email")
        vcard_name_entry.configure(placeholder_text="First and Last Name")
        vcard_phone_entry.configure(placeholder_text="Phone")
        vcard_email_entry.configure(placeholder_text="Email")
    else:
        current_language = "ru"  # Переключить на русский
        title_label.configure(text="Выберите тип QR кода:")
        generate_btn.configure(text="Создать QR")
        lang_btn.configure(text="Сменить язык")
        theme_btn.configure(text="Тёмная тема" if current_theme == "light" else "Светлая тема")
        about_btn.configure(text="О программе")

        # Заполнить плейсхолдеры на русском
        url_entry.configure(placeholder_text="Введите URL")
        ssid_entry.configure(placeholder_text="Имя сети (SSID)")
        wifi_password_entry.configure(placeholder_text="Пароль")
        text_entry.configure(placeholder_text="Введите текст")
        phone_entry.configure(placeholder_text="Введите номер телефона")
        email_entry.configure(placeholder_text="Введите email")
        vcard_name_entry.configure(placeholder_text="Имя и Фамилия")
        vcard_phone_entry.configure(placeholder_text="Телефон")
        vcard_email_entry.configure(placeholder_text="Email")
