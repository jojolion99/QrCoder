# Ветка телефона
    elif qr_type == "Phone":
        number = phone_entry.get()
        if not re.match(r"^\+?[0-9]{7,15}$", number):  # Валидация номера
            show_error("Введите корректный номер..." if current_language == "ru" else "Enter a valid phone number.")
            return
        data = f"tel:{number}"