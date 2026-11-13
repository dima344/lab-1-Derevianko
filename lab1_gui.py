import tkinter as tk
from tkinter import ttk, messagebox

class DiplomaEvaluatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Оцінка дипломного проєкту (Лабораторна робота №1)")
        self.root.geometry("620x480")
        self.root.resizable(False, False)

        self.subsystems = [
            ("1. Відгук керівника", [
                ("Повнота розкриття поставленої задачі", 1, 3, 3),
                ("Технічний рівень виконання роботи", 0, 4, 3),
                ("Самостійність, ініціативність", 0, 2, 2),
                ("Уміння узагальнювати результати існуючих робіт", 0, 2, 1),
                ("Знання з загальнотехнічних і спеціальних дисциплін", 0, 4, 4),
                ("Можливість впровадження матеріалів роботи", 0, 2, 2),
                ("Систематичність роботи, своєчасність виконання", 0, 4, 3),
                ("Зауваження", -2, 0, -1),
                ("Позитивні сторони", 2, 4, 3),
            ]),
            ("2. Рецензія", [
                ("Повнота розкриття теми", 1, 3, 3),
                ("Технічний рівень роботи", 1, 3, 2),
                ("Якість оформлення роботи", 1, 3, 3),
                ("Позитивні сторони роботи", 2, 3, 3),
                ("Можливість впровадження матеріалів проєкту", 0, 3, 2),
            ]),
            ("3. ДЕК", [
                ("Якість доповіді", 0, 20, 18),
                ("Якість презентації", 0, 20, 19),
                ("Відповіді на запитання", 0, 20, 17),
            ])
        ]

        self.entries = []
        self.create_widgets()

    def create_widgets(self):
        top_frame = ttk.Frame(self.root, padding=10)
        top_frame.pack(fill="x")

        ttk.Button(top_frame, text="Тестові дані", command=self.fill_test_data).pack(side="left", padx=5)
        ttk.Button(top_frame, text="Очистити", command=self.clear_data).pack(side="left", padx=5)
        ttk.Button(top_frame, text="Розрахувати результат", command=self.calculate).pack(side="right", padx=5)

        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True, padx=10, pady=5)

        for sub_name, criteria in self.subsystems:
            frame = ttk.Frame(self.notebook, padding=10)
            self.notebook.add(frame, text=sub_name)

            sub_entries = []
            for idx, (crit_name, mn, mx, _) in enumerate(criteria):
                ttk.Label(frame, text=f"{idx+1}. {crit_name} ({mn}..{mx}):").grid(row=idx, column=0, sticky="w", pady=5)
                entry = ttk.Entry(frame, width=10)
                entry.grid(row=idx, column=1, sticky="e", padx=10, pady=5)
                sub_entries.append((crit_name, mn, mx, entry))
            frame.columnconfigure(0, weight=1)
            self.entries.append(sub_entries)

        self.status_label = ttk.Label(self.root, text="Заповніть бали для всіх трьох підсистем", font=("Arial", 10, "bold"), padding=10)
        self.status_label.pack(fill="x")

    def fill_test_data(self):
        for s_idx, (_, criteria) in enumerate(self.subsystems):
            for c_idx, (_, _, _, default_val) in enumerate(criteria):
                entry = self.entries[s_idx][c_idx][3]
                entry.delete(0, tk.END)
                entry.insert(0, str(default_val))
        self.status_label.config(text="Завантажено тестові дані згідно з розрахунком у звіті.")

    def clear_data(self):
        for sub in self.entries:
            for _, _, _, entry in sub:
                entry.delete(0, tk.END)
        self.status_label.config(text="Поля очищено.")

    def calculate(self):
        sums = []
        for s_idx, sub in enumerate(self.entries):
            sub_sum = 0
            for crit_name, mn, mx, entry in sub:
                raw = entry.get().strip()
                try:
                    val = int(raw)
                except ValueError:
                    messagebox.showerror("Помилка введення", f"Підсистема {s_idx+1}, критерій «{crit_name}»:\nвведіть ціле число.")
                    return
                if not (mn <= val <= mx):
                    messagebox.showerror("Помилка діапазону", f"Підсистема {s_idx+1}, критерій «{crit_name}»:\nзначення має бути від {mn} до {mx}.")
                    return
                sub_sum += val
            sums.append(sub_sum)

        s1, s2, s3 = sums
        total = s1 + s2 + s3

        g1 = "Достатньо" if s1 <= 14 else "Задовільно" if s1 <= 17 else "Добре" if s1 <= 20 else "Дуже добре" if s1 <= 23 else "Відмінно"
        g2 = "Задовільно" if s2 <= 9 else "Добре" if s2 <= 13 else "Відмінно"
        g3 = "Достатньо" if s3 <= 24 else "Задовільно" if s3 <= 33 else "Добре" if s3 <= 44 else "Дуже добре" if s3 <= 49 else "Відмінно"
        gt = "Достатньо" if total <= 64 else "Задовільно" if total <= 73 else "Добре" if total <= 83 else "Дуже добре" if total <= 89 else "Відмінно"

        result_text = (
            f"Підсистема 1 (Відгук керівника): {s1} / 25 — {g1}\n"
            f"Підсистема 2 (Рецензія): {s2} / 15 — {g2}\n"
            f"Підсистема 3 (ДЕК): {s3} / 60 — {g3}\n\n"
            f"Інтегральний показник якості: {total} / 100\n"
            f"Підсумкова оцінка: {gt}"
        )
        self.status_label.config(text=f"Загальний бал: {total} / 100 ({gt})")
        messagebox.showinfo("Результати оцінювання", result_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = DiplomaEvaluatorApp(root)
    root.mainloop()