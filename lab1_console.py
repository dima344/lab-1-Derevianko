def get_score(prompt, min_val, max_val):
    while True:
        try:
            val = int(input(f"{prompt} ({min_val}..{max_val}): "))
            if min_val <= val <= max_val:
                return val
            print(f"Помилка: значення має бути в межах від {min_val} до {max_val}.")
        except ValueError:
            print("Помилка: введіть ціле число.")

def grade_p1(score):
    if score <= 14: return "Достатньо"
    if score <= 17: return "Задовільно"
    if score <= 20: return "Добре"
    if score <= 23: return "Дуже добре"
    return "Відмінно"

def grade_p2(score):
    if score <= 9: return "Задовільно"
    if score <= 13: return "Добре"
    return "Відмінно"

def grade_p3(score):
    if score <= 24: return "Достатньо"
    if score <= 33: return "Задовільно"
    if score <= 44: return "Добре"
    if score <= 49: return "Дуже добре"
    return "Відмінно"

def grade_total(score):
    if score <= 64: return "Достатньо"
    if score <= 73: return "Задовільно"
    if score <= 83: return "Добре"
    if score <= 89: return "Дуже добре"
    return "Відмінно"

def main():
    print("=== Моделювання оцінки дипломного проєкту ===")
    
    print("\n--- Підсистема 1. Відгук керівника ---")
    p1_criteria = [
        ("1. Повнота розкриття поставленої задачі", 1, 3),
        ("2. Технічний рівень виконання роботи", 0, 4),
        ("3. Самостійність, ініціативність", 0, 2),
        ("4. Уміння узагальнювати результати існуючих робіт", 0, 2),
        ("5. Знання з загальнотехнічних і спеціальних дисциплін", 0, 4),
        ("6. Можливість впровадження матеріалів роботи", 0, 2),
        ("7. Систематичність роботи, своєчасність виконання", 0, 4),
        ("8. Зауваження", -2, 0),
        ("9. Позитивні сторони", 2, 4),
    ]
    s1 = sum(get_score(name, mn, mx) for name, mn, mx in p1_criteria)
    print(f"Сума за підсистемою 1: {s1} / 25 ({grade_p1(s1)})")

    print("\n--- Підсистема 2. Рецензія ---")
    p2_criteria = [
        ("1. Повнота розкриття теми", 1, 3),
        ("2. Технічний рівень роботи", 1, 3),
        ("3. Якість оформлення роботи", 1, 3),
        ("4. Позитивні сторони роботи", 2, 3),
        ("5. Можливість впровадження матеріалів проєкту", 0, 3),
    ]
    s2 = sum(get_score(name, mn, mx) for name, mn, mx in p2_criteria)
    print(f"Сума за підсистемою 2: {s2} / 15 ({grade_p2(s2)})")

    print("\n--- Підсистема 3. ДЕК ---")
    p3_criteria = [
        ("1. Якість доповіді", 0, 20),
        ("2. Якість презентації", 0, 20),
        ("3. Відповіді на запитання", 0, 20),
    ]
    s3 = sum(get_score(name, mn, mx) for name, mn, mx in p3_criteria)
    print(f"Сума за підсистемою 3: {s3} / 60 ({grade_p3(s3)})")

    total = s1 + s2 + s3
    print("\n==========================================")
    print(f"Інтегральний показник якості: {total} / 100")
    print(f"Підсумкова оцінка: {grade_total(total)}")
    print("==========================================")

if __name__ == "__main__":
    main()