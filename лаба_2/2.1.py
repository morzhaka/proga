def task2():
    # Исходное выражение
    result = 4**2014 + 2**2015 - 8
    
    # Переводим в двоичную систему и считаем единицы
    binary = bin(result)
    ones_count = binary.count('1')
    
    return ones_count

print(task2())