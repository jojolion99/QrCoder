# Обновление текста окна "О программе" при смене языка
def update_about_labels():
    creators_text = "Создатели программы:" if current_language == "ru" else "Program Creators:"
    version_text = "Версия программы: 2.01" if current_language == "ru" else "Program Version: 2.01"
    rights_text = "©Все права защищены" if current_language == "ru" else "©All rights reserved"

    creators_label.configure(text=creators_text)
    version_label.configure(text=version_text)
    rights_label.configure(text=rights_text)