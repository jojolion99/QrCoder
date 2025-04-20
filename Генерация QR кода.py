# Генерация QR-кода
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=2)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color=fill_color, back_color=bg_color)
    img.save("qrcode.png")  # Сохранение изображения

    img_open = Image.open("qrcode.png")  # Открытие изображения
    img_tk = ImageTk.PhotoImage(img_open)  # Преобразование для Tkinter