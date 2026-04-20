

# Есть словарь кодов товаров

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Рассчитать на какую сумму лежит каждого товара на складе
# например для ламп

lamps_cost = store[goods['Лампа']][0]['quantity'] * store[goods['Лампа']][0]['price']
# или проще (/сложнее ?)
lamp_code = goods['Лампа']
lamps_item = store[lamp_code][0]
lamps_quantity = lamps_item['quantity']
lamps_price = lamps_item['price']
lamps_cost = lamps_quantity * lamps_price
print('Лампа -', lamps_quantity, 'шт, стоимость', lamps_cost, 'руб')

# Вывести стоимость каждого вида товара на складе:
# один раз распечать сколько всего столов и их общая стоимость,
# один раз распечать сколько всего стульев и их общая стоимость,
#   и т.д. на складе
# Формат строки <товар> - <кол-во> шт, стоимость <общая стоимость> руб

# WARNING для знающих циклы: БЕЗ циклов. Да, с переменными; да, неэффективно; да, копипаста.
# Это задание на ручное вычисление - что бы потом понять как работают циклы и насколько с ними проще жить.

# TODO здесь ваш код

# Лампа
lamp_code = goods['Лампа']
lamp_q = store[lamp_code][0]['quantity']
lamp_p = store[lamp_code][0]['price']
lamp_total = lamp_q * lamp_p
print('Лампа -', lamp_q, 'шт, стоимость', lamp_total, 'руб')

# Стол
table_code = goods['Стол']
table_q1 = store[table_code][0]['quantity']
table_p1 = store[table_code][0]['price']
table_q2 = store[table_code][1]['quantity']
table_p2 = store[table_code][1]['price']
table_q = table_q1 + table_q2
table_total = (table_q1 * table_p1) + (table_q2 * table_p2)
print('Стол -', table_q, 'шт, стоимость', table_total, 'руб')

# Диван
divan_code = goods['Диван']
divan_q1 = store[divan_code][0]['quantity']
divan_p1 = store[divan_code][0]['price']
divan_q2 = store[divan_code][1]['quantity']
divan_p2 = store[divan_code][1]['price']
divan_q = divan_q1 + divan_q2
divan_total = (divan_q1 * divan_p1) + (divan_q2 * divan_p2)
print('Диван -', divan_q, 'шт, стоимость', divan_total, 'руб')

# Стул
chair_code = goods['Стул']
chair_q1 = store[chair_code][0]['quantity']
chair_p1 = store[chair_code][0]['price']
chair_q2 = store[chair_code][1]['quantity']
chair_p2 = store[chair_code][1]['price']
chair_q3 = store[chair_code][2]['quantity']
chair_p3 = store[chair_code][2]['price']
chair_q = chair_q1 + chair_q2 + chair_q3
chair_total = (chair_q1 * chair_p1) + (chair_q2 * chair_p2) + (chair_q3 * chair_p3)
print('Стул -', chair_q, 'шт, стоимость', chair_total, 'руб')