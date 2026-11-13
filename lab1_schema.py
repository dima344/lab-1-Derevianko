import tkinter as tk

root = tk.Tk()
root.title("Ієрархічна модель оцінки")
root.resizable(False, False)

canvas = tk.Canvas(root, width=780, height=500, bg="white")
canvas.pack()

def draw_box(x1, y1, x2, y2, text, font=("Arial", 10, "bold")):
    canvas.create_rectangle(x1, y1, x2, y2, outline="black", width=2, fill="white")
    canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text=text, font=font, justify="center")

# 1. Мета
draw_box(270, 20, 510, 80, "Мета:\nОцінити дипломний проєкт")

# Підпис рівня
canvas.create_text(390, 102, text="підсистеми", font=("Arial", 9, "italic"))

# Стрілки від Мети до Підсистем
canvas.create_line(330, 80, 130, 130, arrow=tk.LAST, width=1.5)
canvas.create_line(390, 80, 390, 130, arrow=tk.LAST, width=1.5)
canvas.create_line(450, 80, 650, 130, arrow=tk.LAST, width=1.5)

# 2. Підсистеми
draw_box(40, 130, 220, 180, "1. Відгук керівника")
draw_box(300, 130, 480, 180, "2. Рецензія")
draw_box(560, 130, 740, 180, "3. ДЕК")

# Підпис рівня
canvas.create_text(390, 200, text="критерії", font=("Arial", 9, "italic"))

# Стрілки від Підсистем до Критеріїв
canvas.create_line(130, 180, 130, 220, arrow=tk.LAST, width=1.5)
canvas.create_line(390, 180, 390, 220, arrow=tk.LAST, width=1.5)
canvas.create_line(650, 180, 650, 220, arrow=tk.LAST, width=1.5)

# 3. Критерії
c1_text = (
    "1. Повнота розкриття (1–3)\n"
    "2. Технічний рівень (0–4)\n"
    "3. Самостійність (0–2)\n"
    "4. Узагальнення робіт (0–2)\n"
    "5. Знання з дисциплін (0–4)\n"
    "6. Можливість впровадження (0–2)\n"
    "7. Систематичність (0–4)\n"
    "8. Зауваження (-2–0)\n"
    "9. Позитивні сторони (2–4)"
)
draw_box(20, 220, 240, 460, c1_text, font=("Arial", 9))

c2_text = (
    "1. Повнота розкриття (1–3)\n"
    "2. Технічний рівень (1–3)\n"
    "3. Якість оформлення (1–3)\n"
    "4. Позитивні сторони (2–3)\n"
    "5. Можливість впровадження (0–3)"
)
draw_box(280, 220, 500, 370, c2_text, font=("Arial", 9))

c3_text = (
    "1. Доповідь (0–20)\n"
    "2. Презентація (0–20)\n"
    "3. Відповіді (0–20)"
)
draw_box(550, 220, 750, 320, c3_text, font=("Arial", 9))

root.mainloop()