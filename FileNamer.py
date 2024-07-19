import os
import tkinter as tk
from tkinter import filedialog, messagebox

class RenameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Переименование файлов")
        self.root.geometry("400x200")

        self.default_folder = "D:/"
        self.selected_file = None

        # Создаем элементы интерфейса
        self.create_widgets()

    def create_widgets(self):
        self.frame1 = tk.Frame(self.root)
        self.frame1.pack(pady=10)

        self.entry1 = tk.Entry(self.frame1, width=30)
        self.entry1.insert(0, self.default_folder)
        self.entry1.pack(side=tk.LEFT, padx=5)

        self.btn_file = tk.Button(self.frame1, text="Файл", command=self.choose_file)
        self.btn_file.pack(side=tk.LEFT, padx=5)

        self.frame2 = tk.Frame(self.root)
        self.frame2.pack(pady=10)

        self.entry2 = tk.Entry(self.frame2, width=30)
        self.entry2.pack(side=tk.LEFT, padx=5)

        self.btn_start = tk.Button(self.frame2, text="Пуск", command=self.start_renaming, state=tk.DISABLED)
        self.btn_start.pack(side=tk.LEFT, padx=5)

    def choose_file(self):
        self.selected_file = filedialog.askopenfilename(initialdir=self.default_folder)
        if self.selected_file:
            self.entry1.delete(0, tk.END)
            self.entry1.insert(0, self.selected_file)
            self.btn_start.config(state=tk.NORMAL)

    def start_renaming(self):
        start_number = self.entry2.get()
        if not start_number.isdigit():
            messagebox.showerror("Ошибка", "Введите корректное число")
            return

        start_number = int(start_number)
        folder = os.path.dirname(self.selected_file)
        files = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
        
        # Отфильтровываем файлы, которые начинаются с цифры
        files_to_rename = [f for f in files if not f[0].isdigit()][:10]

        for i, file in enumerate(files_to_rename):
            extension = os.path.splitext(file)[1]
            new_name = f"{start_number + i}{extension}"
            old_file_path = os.path.join(folder, file)
            new_file_path = os.path.join(folder, new_name)

            try:
                os.rename(old_file_path, new_file_path)
                print(f"Файл {old_file_path} переименован в {new_file_path}")
            except Exception as e:
                print(f"Ошибка при переименовании {old_file_path}: {e}")

        messagebox.showinfo("Успех", "Переименование завершено")

if __name__ == "__main__":
    root = tk.Tk()
    app = RenameApp(root)
    root.mainloop()
