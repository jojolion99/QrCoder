# Список авторов
name_labels = [
    customtkinter.CTkLabel(about_window, text="Бабаев Тимур Русланович", font=font_family),
    customtkinter.CTkLabel(about_window, text="Антоненко Артём Алексеевич", font=font_family),
    customtkinter.CTkLabel(about_window, text="Евсеев Артём Романович", font=font_family),
    customtkinter.CTkLabel(about_window, text="Краснов Андрей Константинович", font=font_family),
]
for label in name_labels:
    label.pack()

version_label = customtkinter.CTkLabel(about_window, font=(font_family[0], 12))
version_label.pack()

rights_label = customtkinter.CTkLabel(about_window, font=(font_family[0], 12), text_color="#AAAAAA")
rights_label.pack(side="bottom", pady=10)

update_about_labels()
