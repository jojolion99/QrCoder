# Кнопки PNG и PDF
customtkinter.CTkButton(qr_window, text="Скачать PNG" if current_language == "ru" else "Download PNG",
                        command=download_png, font=font_family).pack(pady=5)
customtkinter.CTkButton(qr_window, text="Экспорт в PDF" if current_language == "ru" else "Export to PDF",
                        command=export_pdf, font=font_family).pack(pady=5)
