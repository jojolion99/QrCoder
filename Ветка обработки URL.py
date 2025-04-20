# Ветка обработки URL
    if qr_type == "URL":
        data = url_entry.get()
        # Валидация URL
        if not data or not re.match(r"^(https?|ftp)://[^\s]+$", data):
            show_error("Ошибка, введите корректную ссылку." if current_language == "ru" else "Error, enter a valid URL.")
            return