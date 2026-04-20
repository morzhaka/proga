def split_recursive_simple(lst, n):
    # Базовый случай: пустой список
    if not lst:
        return [[] for _ in range(n)]
    
    # Рекурсивно обрабатываем список без последнего элемента
    rest = split_recursive_simple(lst[:-1], n)
    
    # Добавляем последний элемент в нужную часть
    rest[(len(lst) - 1) % n].append(lst[-1])
    
    return rest

# Выводим результат
print(split_recursive_simple([1, 2, 3, 4, 5], 2))
print(split_recursive_simple([1, 2, 3, 4, 5], 3))