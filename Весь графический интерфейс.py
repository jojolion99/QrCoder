# --- Графический интерфейс ---

root = customtkinter.CTk()  # Главное окно
root.title("Генератор QR Кодов")  # Название окна
root.geometry("600x450")  # Размеры
root.resizable(False, False)  # Запрет изменения размеров
root.attributes('-fullscreen', False)  # Не в полноэкранном режиме

# Верхняя панель кнопок: язык, тема, о программе
top_buttons_frame = customtkinter.CTkFrame(root, fg_color="transparent")
top_buttons_frame.pack(pady=5)

lang_btn = customtkinter.CTkButton(top_buttons_frame, text="Сменить язык", command=switch_language, font=font_family)
lang_btn.pack(side="left", padx=10)

theme_btn = customtkinter.CTkButton(top_buttons_frame, text="Тёмная тема", command=toggle_theme, font=font_family)
theme_btn.pack(side="left", padx=10)

about_btn = customtkinter.CTkButton(top_buttons_frame, text="О программе", command=show_about, font=font_family)
about_btn.pack(side="left", padx=10)

# Заголовок
title_label = customtkinter.CTkLabel(root, text="Выберите тип QR кода:", font=font_family)
title_label.pack(pady=8)

# Меню выбора типа QR-кода
qr_type_var = tk.StringVar(value="URL")  # Значение по умолчанию
qr_type_menu = customtkinter.CTkOptionMenu(root, values=["URL", "WiFi", "Text", "Phone", "Email", "VCard"],
                                           variable=qr_type_var, command=switch_inputs, font=font_family)
qr_type_menu.pack(pady=5)

# Фрейм с полями ввода
input_frame = customtkinter.CTkFrame(root)
input_frame.pack(pady=10)

# Поля ввода
url_entry = customtkinter.CTkEntry(input_frame, placeholder_text="Введите URL", font=font_family, width=225)
ssid_entry = customtkinter.CTkEntry(input_frame, placeholder_text="Имя сети (SSID)", font=font_family, width=225)
wifi_password_entry = customtkinter.CTkEntry(input_frame, placeholder_text="Пароль", font=font_family, width=225)
auth_type_var = tk.StringVar(value="WPA")
auth_type_menu = customtkinter.CTkOptionMenu(input_frame, values=["WPA", "WEP", "nopass"], variable=auth_type_var, font=font_family, width=225)

text_entry = customtkinter.CTkEntry(input_frame, placeholder_text="Введите текст", font=font_family, width=225)
phone_entry = customtkinter.CTkEntry(input_frame, placeholder_text="Введите номер телефона", font=font_family, width=225)
email_entry = customtkinter.CTkEntry(input_frame, placeholder_text="Введите email", font=font_family, width=225)

vcard_name_entry = customtkinter.CTkEntry(input_frame, placeholder_text="Имя и Фамилия", font=font_family, width=225)
vcard_phone_entry = customtkinter.CTkEntry(input_frame, placeholder_text="Телефон", font=font_family, width=225)
vcard_email_entry = customtkinter.CTkEntry(input_frame, placeholder_text="Email", font=font_family, width=225)

# Фрейм для выбора цветов
color_frame = customtkinter.CTkFrame(root)
color_frame.pack(pady=10)

# Переменные для хранения цвета
qr_color = tk.StringVar(value="black")
bg_color_var = tk.StringVar(value="white")

# Кнопки выбора цвета QR и фона
customtkinter.CTkButton(color_frame, text="Цвет QR", command=lambda: qr_color.set(colorchooser.askcolor()[1]), font=font_family).pack(side="left", padx=10)
customtkinter.CTkButton(color_frame, text="Цвет фона", command=lambda: bg_color_var.set(colorchooser.askcolor()[1]), font=font_family).pack(side="left", padx=10)

# Кнопка генерации QR-кода
generate_btn = customtkinter.CTkButton(root, text="Создать QR", command=generate_qr_code, font=font_family)
generate_btn.pack(pady=10)

switch_inputs()  # Показываем поля по умолчанию
root.mainloop()  # Запускаем основной цикл