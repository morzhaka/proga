<img width="1278" height="912" alt="Снимок экрана 2026-04-15 131247" src="https://github.com/user-attachments/assets/05c0dd12-05fb-4ec1-8c91-cadb5e0e10a2" /># proga
# Отчёт по лабораторной работе №1

## Задание 1 
Вычислить расстояния между городами Moscow, London, Paris по их координатам. Результат сохранить в словарь distances и вывести на экран.

## Описание проделанной работы
Была написана программа на Python, которая:
1. Содержит словарь sites с координатами трёх городов
2. Создаёт пустой словарь distances для результатов
3. Перебирает все уникальные пары городов
4. Вычисляет расстояние между каждой парой по формуле: √((x₂-x₁)² + (y₂-y₁)²)
5. Сохраняет результат в словарь distances
6. Выводит полученный словарь на экран

### Код программы:
```python
sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480)
}

distances = {}

cities = list(sites.keys())

for i in range(len(cities)):
    for j in range(i + 1, len(cities)):
        city1 = cities[i]
        city2 = cities[j]
        
        x1, y1 = sites[city1]
        x2, y2 = sites[city2]
        
        distance = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5
        
        distances[(city1, city2)] = distance

print(distances)

Результат выполнения

{('Moscow', 'London'): 145.60219778561037, ('Moscow', 'Paris'): 130.38404810405297, ('London', 'Paris'): 42.42640687119285}

Шпаргалка по командам git
Команда	Описание
git clone <url>	Клонировать репозиторий с GitHub
git status	Проверить состояние файлов
git add <файл>	Добавить файл для коммита
git add .	Добавить все изменённые файлы
git commit -m "текст"	Сохранить изменения с комментарием
git push	Отправить изменения на GitHub
git pull	Скачать изменения с GitHub

Скриншот

<img width="1278" height="912" alt="Снимок экрана 2026-04-15 131247" src="https://github.com/user-attachments/assets/807b99c3-99ed-45d0-b003-f40347a2950f" />


## Ссылки на используемые материалы


- [Документация Python](https://docs.python.org/3/)
- [Формула расстояния между точками](https://ru.wikipedia.org/wiki/Расстояние_между_двумя_точками)
- [Шпаргалка по Git](https://git-scm.com/doc)
