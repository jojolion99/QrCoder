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
