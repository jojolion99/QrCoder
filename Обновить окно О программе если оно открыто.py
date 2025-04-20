# Обновить окно "О программе", если оно открыто
if "about_window" in globals() and about_window.winfo_exists():
    update_about_labels()