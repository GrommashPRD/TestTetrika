from task1.solution import strict

@strict
def sum_two(a: int, b: int) -> int:
    return a + b

def test_sum_two():
    # Тест 1: корректные типы
    try:
        result = sum_two(1, 2)
        assert result == 3, "Тест не пройден! Ожидалось 3."
        print("Тест 1 пройден!")
    except Exception as e:
        print(f"Тест 1 провалился. Ошибка: {e}")

    # Тест 2: неверный тип первого аргумента
    try:
        sum_two('1', 2)
        print("Тест 2 провалился, исключение не вызвано.")
    except TypeError as e:
        print(f"Тест 2 пройден! Ошибка: {e}")

    # Тест 3: неверный тип второго аргумента
    try:
        sum_two(1, 2.4)
        print("Тест 3 провалился, исключение не вызвано.")
    except TypeError as e:
        print(f"Тест 3 пройден! Ошибка: {e}")

    # Тест 4: отсутствие обязательных аргументов
    try:
        sum_two(1)  # только один аргумент
        print("Тест 4 провалился, исключение не вызвано.")
    except TypeError as e:
        print(f"Тест 4 пройден! Ошибка: {e}")

    # Тест 5: лишние аргументы
    try:
        sum_two(1, 2, 3)  # три аргумента вместо двух
        print("Тест 5 провалился, исключение не вызвано.")
    except TypeError as e:
        print(f"Тест 5 пройден! Ошибка: {e}")

# Запуск тестов
test_sum_two()