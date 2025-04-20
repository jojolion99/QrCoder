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