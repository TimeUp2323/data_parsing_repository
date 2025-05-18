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

        self.run_btn = ttk.Button(
            self,
            text="Старт",
            command=self.run_processing
        )
        self.run_btn.pack()

    def _setup_menu(self):
        menu = tk.Menu(self)
        menu.add_command(label="Справка", command=self.show_help)
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
        messagebox.showinfo("Справка", text)

    def show_about(self):
        text = "Парсер файлов версия 1.0"
        messagebox.showinfo("О программе", text)

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()