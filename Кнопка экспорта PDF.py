# Кнопка экспорта PDF
def export_pdf():
    path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])
    if path:
        pdf = FPDF()
        pdf.add_page()
        pdf.image("qrcode.png", x=60, y=50, w=90)
        pdf.output(path)
        messagebox.showinfo("Сохранено" if current_language == "ru" else "Saved", f"PDF сохранен: {path}")
