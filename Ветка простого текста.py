# Ветка простого текста
    elif qr_type == "Text":
        data = text_entry.get()
        if not data or re.search(r"https?://", data):  # Без ссылок
            show_error("Введите обычный текст..." if current_language == "ru" else "Enter plain text...")
            return