import tkinter as tk
from tkinter import ttk


class ResultWindow(tk.Toplevel):
    def __init__(self, parent, handler):
        super().__init__(parent)
        self.parent = parent
        self.title("Результаты")
        self.geometry("860x600")

        self.configure(bg=parent.result_window_bg)

        main_frame = ttk.Frame(self)
        main_frame.pack(fill="both", expand=True, padx=5, pady=5)

        text_frame = ttk.Frame(main_frame)
        text_frame.pack(fill="both", expand=True)

        self.text = tk.Text(
            text_frame,
            wrap='word',
            bg=parent.result_window_bg,
            fg=parent.result_window_fg,
        )

        scroll = ttk.Scrollbar(text_frame, command=self.text.yview)

        self.text.configure(yscrollcommand=scroll.set)

        scroll.pack(side='right', fill='y')
        self.text.pack(side='left', fill='both', expand=True)

        button_frame = ttk.Frame(main_frame)
        button_frame.pack(fill='x', pady=(5, 0))

        close_button = ttk.Button(
            button_frame,
            text="Начать новый анализ",
            command=self.destroy
        )
        close_button.pack(pady=5)

        self._show_results(handler)

    def _show_results(self, handler):
        self.text.insert('end', "Статистика обработки:\n")
        self.text.insert('end', f"Найдено всего файлов: {handler.get_count_files()}\n")
        self.text.insert('end', f"Найдено всего разрешений:\n")
        for i, ext in enumerate(handler.get_extensions()):
            self.text.insert('end', f"{i +1} {ext}: {handler.get_extensions()[ext]}\n")

    def update_theme_result_window(self):
        """Обновляет цвета в соответствии с текущей темой."""
        self.configure(bg=self.parent.result_window_bg)
        self.text.configure(
            bg=self.parent.result_window_bg,
            fg=self.parent.result_window_fg
        )