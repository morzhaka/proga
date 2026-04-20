import itertools

def task1():
    # Доступные буквы
    letters = ['В', 'И', 'Ш', 'Н', 'Я']
    # Гласные (нельзя заканчивать на них)
    vowels = ['И', 'Я']
    count = 0
    
    # Перебираем все возможные 6-буквенные комбинации
    for word_tuple in itertools.product(letters, repeat=6):
        word = ''.join(word_tuple)
        
        # Не начинается с Ш
        if word[0] == 'Ш':
            continue
        # Не оканчивается на гласную
        if word[-1] in vowels:
            continue
        # Буква В не более одного раза
        if word.count('В') > 1:
            continue
        
        count += 1
    
    return count

print(task1())