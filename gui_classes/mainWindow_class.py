import tkinter as tk
from tkinter import ttk, messagebox
from fileHandler_class import FileHandler
from resultWindow_class import ResultWindow
from tkinter import Toplevel, Text, END
import webbrowser


def show_details():
    help_window = Toplevel()
    help_window.title("Подробнее")
    help_window.geometry("500x400")

    text_widget = Text(help_window, wrap="word", padx=20, pady=20)

    text_widget.tag_configure("title", font=("Arial", 14, "bold"), justify='center')
    text_widget.tag_configure("normal", font=("Arial", 11), justify='center')
    text_widget.tag_configure("bold", font=("Arial", 11, "bold"))
    text_widget.tag_configure("italic", font=("Arial", 11, "italic"))
    text_widget.tag_configure("link", font=("Arial", 11, "underline"), foreground="blue")

    text_widget.insert(END, "Обратная связь\n", "title")
    text_widget.insert(END, "timeupwork6432@gmail.com\n", ("timeupwork6432@gmail.com", "normal", "link"))
    text_widget.insert(END, "Telegram\n\n", ("https://t.me/timeup6432", "normal", "link"))

    text_widget.insert(END, "Исходный код\n", "title")
    text_widget.insert(END, "GitHub репозиторий проекта\n\n", ("https://github.com/TimeUp2323/data_parsing_repository", "normal", "link"))

    text_widget.insert(END, "Источники\n", "title")
    text_widget.insert(END, "Использованные материалы\n\n",("https://metanit.com", "normal", "link"))


    def make_link_clickable(url):
        def callback(event):
            webbrowser.open_new(url)

        return callback

    for url in ["https://github.com/TimeUp2323/data_parsing_repository",
                "https://dev.to/username",
                "https://metanit.com",
                "timeupwork6432@gmail.com",
                "https://t.me/timeup6432"]:
        text_widget.tag_bind(url, "<Button-1>", make_link_clickable(url))

    text_widget.config(state="disabled")
    text_widget.pack(fill="both", expand=True)

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Главное окно")
        self.geometry("560x480")
        self.file_handler = FileHandler()

        self.dark_mode = False

        self._create_widgets()
        self._setup_menu()
        self._set_theme()

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

        self.theme_btn = ttk.Button(
            self,
            text="Тёмная тема",
            command=self.toggle_theme
        )
        self.theme_btn.pack(pady=10)

    def toggle_theme(self):
        self.dark_mode = not self.dark_mode
        self._set_theme()
        self.theme_btn.config(text="Тёмная тема" if not self.dark_mode else "Светлая тема")

    def _set_theme(self):
        if self.dark_mode:
            self.configure(bg='#2d2d2d')
            style = ttk.Style()
            style.theme_use('clam')

            style.configure('.', background='#2d2d2d', foreground='white')
            style.configure('TEntry', fieldbackground='#3d3d3d', foreground='white')
            style.configure('TButton', background='#3d3d3d', foreground='white')
            style.configure('TLabel', background='#2d2d2d', foreground='white')
            style.configure('TText', background='#3d3d3d', foreground='white')

            self.result_window_bg = '#3d3d3d'
            self.result_window_fg = 'white'

        else:
            self.configure(bg='SystemButtonFace')
            style = ttk.Style()
            style.theme_use('clam')

            style.configure('.', background='SystemButtonFace', foreground='black')
            style.configure('TEntry', fieldbackground='white', foreground='black')
            style.configure('TButton', background='SystemButtonFace', foreground='black')
            style.configure('TLabel', background='SystemButtonFace', foreground='black')
            style.configure('TText', background='white', foreground='black')

            # Для ResultWindow
            self.result_window_bg = 'white'
            self.result_window_fg = 'black'

        for window in self.winfo_children():
            if isinstance(window, ResultWindow):
                window.update_theme_result_window()

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
        menu.add_command(label="Подробнее", command=show_details)
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

    def show_about(self):
        feedback = "Парсер файлов версия 2.3.0"
        messagebox.showinfo("О программе", feedback )



if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()