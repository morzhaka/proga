# 1. Ваше замыкание (упрощенное)
def range_checker(min_val, max_val):
    def check(number):
        if not (min_val <= number <= max_val):
            # Специально вызываем ошибку, чтобы декоратор её поймал
            raise ValueError("Число вне диапазона")
        return "Число " + str(number) + " в порядке"
    return check

#  упрощенный декоратор
def error_handler(func):
    def wrapper(number):
        try:
            return func(number)
        except Exception:
            return "Произошла ошибка"
    return wrapper


# Шаг 1: Создаем само замыкание (диапазон от 0 до 120)
my_check = range_checker(0, 120)

# Шаг 2: Применяем декоратор к этому замыканию
# Теперь "safe_check" - это обернутая функция
safe_check = error_handler(my_check)

# Шаг 3: Тестируем работу
print(safe_check(50))   # Выведет: Число 50 в порядке
print(safe_check(150))  # Выведет: Произошла ошибка