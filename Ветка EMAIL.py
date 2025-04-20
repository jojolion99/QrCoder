# Ветка Email
    elif qr_type == "Email":
        email = email_entry.get()
        if not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email):
            show_error("Введите корректный email." if current_language == "ru" else "Enter a valid email.")
            return
        data = f"mailto:{email}"