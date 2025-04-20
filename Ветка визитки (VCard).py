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