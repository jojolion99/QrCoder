# Кнопка сохранения PNG
def download_png():
    path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Files", "*.png")])
    if path:
        img.save(path)
        messagebox.showinfo("Сохранено" if current_language == "ru" else "Saved", f"Сохранено: {path}")
