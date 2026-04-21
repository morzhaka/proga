def error_handler(func):
    def wrapper(number):
        try:
            return func(number)
        except Exception:
            return "Произошла ошибка"
    return wrapper