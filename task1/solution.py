import inspect
import functools


def strict(func):
    sig = inspect.signature(func)

    annotations = func.__annotations__

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        bound_args = sig.bind(*args, **kwargs)

        for param_name, value in bound_args.arguments.items():
            if param_name in annotations:
                expected_type = annotations[param_name]
                actual_type = type(value)

                if actual_type is not expected_type:
                    raise TypeError(
                        f"'{param_name}' для '{func.__name__}' должен быть типа "
                        f"{expected_type.__name__}, а не {actual_type.__name__}."
                    )
        return func(*args, **kwargs)
    return wrapper

@strict
def sum_two(a: int, b: int) -> int:
    return a + b

def test_sum_two():
    try:
        result = sum_two(1, 2)
        assert result == 3, "Тест не прошел. Ожидалось 3."
        print("Тест 1 прошел.")
    except Exception as e:
        print(f"Тест 1 не прошел. Ошибка: {e}")

    try:
        sum_two('1', 2)
        print("Тест 2 не прошел, исключение не вызвано.")
    except TypeError as e:
        print(f"Тест 2 прошел. Ошибка: {e}")

    try:
        sum_two(1, 2.4)
        print("Тест 3 не прошел, исключение не вызвано.")
    except TypeError as e:
        print(f"Тест 3 прошел. Ошибка: {e}")

    try:
        sum_two(1)
        print("Тест 4 не прошел. Исключение не вызвано.")
    except TypeError as er:
        print(f"Тест 4 прошел. Ошибка: {er}")

    try:
        sum_two(1, 2, 3)
        print("Тест 5 не прошел, исключение не вызвано.")
    except TypeError as er:
        print(f"Тест 5 прошел. Ошибка: {er}")

test_sum_two()