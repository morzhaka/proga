def range_checker(min_val, max_val):
    def check(number):
        if not (min_val <= number <= max_val):
            raise ValueError("Число " + str(number) + " не входит в диапазон от " + str(min_val) + " до " + str(max_val))
        return "Число " + str(number) + " в порядке"
    return check

# СОЗДАЕМ замыкание (это просто подготовка)
check_age = range_checker(0, 120)

# ВЫЗЫВАЕМ замыкание (вот тут появляется результат)
print(check_age(50))   
print(check_age(150))  