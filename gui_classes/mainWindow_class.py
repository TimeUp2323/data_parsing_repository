import tkinter as tk
from tkinter import ttk, messagebox
from fileHandler_class import FileHandler
from resultWindow_class import ResultWindow

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Главное окно")
        self.geometry("560x480")
        self.file_handler = FileHandler()

        self._create_widgets()
        self._setup_menu()

    def _create_widgets(self):
        self.entry = ttk.Entry(self, width=50)
        self.entry.pack(pady=140, padx=50)

        self.entry.insert(0, "Введите абсолютный путь к директории ...")
        self.entry.config(foreground="grey")

        self.entry.bind("<FocusIn>", self._clear_placeholder)
        self.entry.bind("<FocusOut>", self._set_placeholder)

        self.run_btn = ttk.Button(
            self,
            text="Старт",
            command=self.run_processing
        )
        self.run_btn.pack()

    def _clear_placeholder(self, event):
        if self.entry.get() == "Введите абсолютный путь к директории ...":
            self.entry.delete(0, "end")
            self.entry.config(foreground="black")

    def _set_placeholder(self, event):
        if not self.entry.get():
            self.entry.insert(0, "Введите абсолютный путь к директории ...")
            self.entry.config(foreground='grey')


    def _setup_menu(self):
        menu = tk.Menu(self)
        menu.add_command(label="Подробнее", command=self.show_help)
        menu.add_command(label="О программе", command=self.show_about)
        self.config(menu=menu)

    def run_processing(self):
        path = self.entry.get()
        if not path:
            messagebox.showerror("Ошибка", "Введите путь директории")
            return
        try:
            self.file_handler.process_all_directories(path)
            ResultWindow(self, self.file_handler)
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))

    def show_help(self):
        text = "Введите путь к директории и нажмите 'Старт'"
        messagebox.showinfo("Подробнее", text)

    def show_about(self):
        feedback = "Парсер файлов версия 1.0 \n Для обратной связи: timeupwork6432@gmail.com"
        messagebox.showinfo("О программе", feedback )

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()