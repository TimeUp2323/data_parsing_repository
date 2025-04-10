import tkinter as tk
from tkinter import ttk


class ResultWindow(tk.Toplevel):
    def __init__(self, parent, handler):
        super().__init__(parent)
        self.title("Результаты")
        self.geometry("860x600")

        text_frame = ttk.Frame(self)
        text_frame.pack(fill="both", expand=True)

        self.text = tk.Text(text_frame, wrap='word')
        scroll = ttk.Scrollbar(text_frame, command=self.text.yview)

        self.text.configure(yscrollcommand=scroll.set)

        scroll.pack(side='right', fill='y')
        self.text.pack(side='left', fill='both', expand=True)

        self._show_results(handler)

    def _show_results(self, handler):
        self.text.insert('end', "Статистика обработки:\n")
        self.text.insert('end', f"Найдено всего файлов: {handler._count_files}\n")
        self.text.insert('end', f"Расширения файлов: {handler._extensions}\n\n")