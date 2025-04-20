# Показывает окно "О программе"
def show_about():
    global about_window
    if "about_window" in globals() and about_window.winfo_exists():
        update_about_labels()
        return

    about_window = customtkinter.CTkToplevel(root)
    about_window.title("О программе" if current_language == "ru" else "About")
    about_window.geometry("400x280")
    about_window.resizable(False, False)

    global creators_label, name_labels, version_label, rights_label
