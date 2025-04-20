# Функция генерации QR-кода
def generate_qr_code():
    qr_type = qr_type_var.get()  # Получение выбранного типа QR
    fill_color = qr_color.get()  # Цвет QR
    bg_color = bg_color_var.get()  # Цвет фона