# Импорт стандартных и сторонних библиотек
import tkinter as tk  # Стандартная библиотека для GUI
from tkinter import messagebox, filedialog, colorchooser  # Диалоги и выбор цвета
import qrcode  # Генерация QR-кодов
from PIL import ImageTk, Image  # Работа с изображениями
from fpdf import FPDF  # Генерация PDF
import customtkinter  # Расширенная версия Tkinter с поддержкой тем и стилей
import re  # Регулярные выражения

# Настройки темы для customtkinter
customtkinter.set_appearance_mode("System")  # Системная тема
customtkinter.set_default_color_theme("blue")  # Цветовая тема интерфейса

# Глобальные переменные для языка и темы
current_language = "ru"  # Язык по умолчанию — русский
current_theme = "light"  # Светлая тема по умолчанию

# Шрифт интерфейса
font_family = ("TTFirsNeue-DemiBold", 14)

# Функция генерации QR-кода
def generate_qr_code():
    qr_type = qr_type_var.get()  # Получение выбранного типа QR
    fill_color = qr_color.get()  # Цвет QR
    bg_color = bg_color_var.get()  # Цвет фона

    # Ветка обработки URL
    if qr_type == "URL":
        data = url_entry.get()
        # Валидация URL
        if not data or not re.match(r"^(https?|ftp)://[^\s]+$", data):
            show_error("Ошибка, введите корректную ссылку." if current_language == "ru" else "Error, enter a valid URL.")
            return

    # Ветка WiFi
    elif qr_type == "WiFi":
        ssid = ssid_entry.get()
        password = wifi_password_entry.get()
        auth = auth_type_var.get()
        if not ssid or not re.match(r"^[\w\s-]+$", ssid):  # Проверка SSID
            show_error("Введите корректный SSID..." if current_language == "ru" else "Enter valid SSID...")
            return
        if password and not re.match(r"^[\w\s\-!@#$%^&*()_+=]{4,}$", password):  # Проверка пароля
            show_error("Пароль WiFi должен быть от 4 символов..." if current_language == "ru" else "WiFi password must be 4+...")
            return
        data = f"WIFI:T:{auth};S:{ssid};P:{password};;"

    # Ветка простого текста
    elif qr_type == "Text":
        data = text_entry.get()
        if not data or re.search(r"https?://", data):  # Без ссылок
            show_error("Введите обычный текст..." if current_language == "ru" else "Enter plain text...")
            return

    # Ветка телефона
    elif qr_type == "Phone":
        number = phone_entry.get()
        if not re.match(r"^\+?[0-9]{7,15}$", number):  # Валидация номера
            show_error("Введите корректный номер..." if current_language == "ru" else "Enter a valid phone number.")
            return
        data = f"tel:{number}"

    # Ветка Email
    elif qr_type == "Email":
        email = email_entry.get()
        if not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email):
            show_error("Введите корректный email." if current_language == "ru" else "Enter a valid email.")
            return
        data = f"mailto:{email}"

    # Ветка визитки (vCard)
    elif qr_type == "VCard":
        fn = vcard_name_entry.get()
        phone = vcard_phone_entry.get()
        email = vcard_email_entry.get()
        if not fn.strip():
            show_error("Имя не может быть пустым." if current_language == "ru" else "Name cannot be empty.")
            return
        if not re.match(r"^\+?[0-9]{7,15}$", phone):
            show_error("Введите корректный номер..." if current_language == "ru" else "Enter valid phone...")
            return
        if not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email):
            show_error("Введите корректный email." if current_language == "ru" else "Enter valid email.")
            return
        data = f"BEGIN:VCARD\nVERSION:3.0\nFN:{fn}\nTEL:{phone}\nEMAIL:{email}\nEND:VCARD"

    else:
        show_error("Неизвестный тип данных." if current_language == "ru" else "Unknown data type.")
        return

    # Генерация QR-кода
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=2)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color=fill_color, back_color=bg_color)
    img.save("qrcode.png")  # Сохранение изображения

    img_open = Image.open("qrcode.png")  # Открытие изображения
    img_tk = ImageTk.PhotoImage(img_open)  # Преобразование для Tkinter

    # Создание нового окна с QR-кодом
    qr_window = customtkinter.CTkToplevel(root)
    qr_window.title("QR Код" if current_language == "ru" else "QR Code")
    qr_window.geometry(f"{img_open.width + 60}x{img_open.height + 130}")
    qr_window.resizable(False, False)

    # Отображение изображения
    label = customtkinter.CTkLabel(qr_window, image=img_tk, text="")
    label.image = img_tk
    label.pack(pady=20)

    # Кнопка сохранения PNG
    def download_png():
        path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Files", "*.png")])
        if path:
            img.save(path)
            messagebox.showinfo("Сохранено" if current_language == "ru" else "Saved", f"Сохранено: {path}")

    # Кнопка экспорта PDF
    def export_pdf():
        path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])
        if path:
            pdf = FPDF()
            pdf.add_page()
            pdf.image("qrcode.png", x=60, y=50, w=90)
            pdf.output(path)
            messagebox.showinfo("Сохранено" if current_language == "ru" else "Saved", f"PDF сохранен: {path}")

    # Кнопки PNG и PDF
    customtkinter.CTkButton(qr_window, text="Скачать PNG" if current_language == "ru" else "Download PNG", command=download_png, font=font_family).pack(pady=5)
    customtkinter.CTkButton(qr_window, text="Экспорт в PDF" if current_language == "ru" else "Export to PDF", command=export_pdf, font=font_family).pack(pady=5)

# Показывает всплывающее окно с ошибкой
def show_error(msg):
    messagebox.showerror("Ошибка" if current_language == "ru" else "Error", msg)

# Показывает окно "О программе"
def show_about():
    global about_window
    if "about_window" in globals() and about_window.winfo_exists():
        update_about_labels()
        return

    about_window = customtkinter.CTkToplevel(root)
    about_window.title("О программе" if current_language == "ru" else "About")
    about_window.geometry("400x280")
    about_window.resizable(False, False)

    global creators_label, name_labels, version_label, rights_label

    # Элементы интерфейса
    creators_label = customtkinter.CTkLabel(about_window, font=font_family)
    creators_label.pack(pady=(15, 5))

    # Список авторов
    name_labels = [
        customtkinter.CTkLabel(about_window, text="Бабаев Тимур Русланович", font=font_family),
        customtkinter.CTkLabel(about_window, text="Антоненко Артём Алексеевич", font=font_family),
        customtkinter.CTkLabel(about_window, text="Евсеев Артём Романович", font=font_family),
        customtkinter.CTkLabel(about_window, text="Краснов Андрей Константинович", font=font_family),
    ]
    for label in name_labels:
        label.pack()

    version_label = customtkinter.CTkLabel(about_window, font=(font_family[0], 12))
    version_label.pack()

    rights_label = customtkinter.CTkLabel(about_window, font=(font_family[0], 12), text_color="#AAAAAA")
    rights_label.pack(side="bottom", pady=10)

    update_about_labels()

# Обновление текста окна "О программе" при смене языка
def update_about_labels():
    creators_text = "Создатели программы:" if current_language == "ru" else "Program Creators:"
    version_text = "Версия программы: 2.01" if current_language == "ru" else "Program Version: 2.01"
    rights_text = "©Все права защищены" if current_language == "ru" else "©All rights reserved"

    creators_label.configure(text=creators_text)
    version_label.configure(text=version_text)
    rights_label.configure(text=rights_text)

# Функция переключения видимых полей ввода в зависимости от выбранного типа QR-кода
def switch_inputs(*args):
    for widget in input_frame.winfo_children():
        widget.pack_forget()  # Скрыть все текущие поля

    t = qr_type_var.get()  # Получить выбранный тип

    # Показать соответствующие поля
    if t == "URL":
        url_entry.pack(pady=5)
    elif t == "WiFi":
        ssid_entry.pack(pady=5)
        wifi_password_entry.pack(pady=5)
        auth_type_menu.pack(pady=5)
    elif t == "Text":
        text_entry.pack(pady=5)
    elif t == "Phone":
        phone_entry.pack(pady=5)
    elif t == "Email":
        email_entry.pack(pady=5)
    elif t == "VCard":
        vcard_name_entry.pack(pady=5)
        vcard_phone_entry.pack(pady=5)
        vcard_email_entry.pack(pady=5)

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

    # Обновить окно "О программе", если оно открыто
    if "about_window" in globals() and about_window.winfo_exists():
        update_about_labels()

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
