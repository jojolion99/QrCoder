# Функция переключения видимых полей ввода в зависимости от выбранного типа QR-кода
def switch_inputs(*args):
    for widget in input_frame.winfo_children():
        widget.pack_forget()  # Скрыть все текущие поля

    t = qr_type_var.get()  # Получить выбранный тип