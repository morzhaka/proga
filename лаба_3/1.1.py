def split_simple(lst, n):
    # Создаём n пустых списков
    result = []
    for i in range(n):
        result.append([])
    
    # Распределяем элементы
    for i in range(len(lst)):
        result[i % n].append(lst[i])
    
    return result

# Выводим результат
print(split_simple([1, 2, 3, 4, 5], 2))
print(split_simple([1, 2, 3, 4, 5], 3))