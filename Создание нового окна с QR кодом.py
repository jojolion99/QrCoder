# Создание нового окна с QR-кодом
    qr_window = customtkinter.CTkToplevel(root)
    qr_window.title("QR Код" if current_language == "ru" else "QR Code")
    qr_window.geometry(f"{img_open.width + 60}x{img_open.height + 130}")
    qr_window.resizable(False, False)