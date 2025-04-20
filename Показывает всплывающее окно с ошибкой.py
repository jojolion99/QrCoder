# Показывает всплывающее окно с ошибкой
def show_error(msg):
    messagebox.showerror("Ошибка" if current_language == "ru" else "Error", msg)