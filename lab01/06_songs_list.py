

violator_songs_list = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83],
]

# Время трёх песен из списка
a = violator_songs_list[3][1]  # Halo
b = violator_songs_list[5][1]  # Enjoy the Silence
c = violator_songs_list[8][1]  # Clean
total1 = a + b + c
print('Три песни звучат', round(total1, 2), 'минут')

violator_songs_dict = {
    'World in My Eyes': 4.76,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.30,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.6,
    'Policy of Truth': 4.88,
    'Blue Dress': 4.18,
    'Clean': 5.68,
}

# Время трёх песен из словаря
x = violator_songs_dict['Sweetest Perfection']
y = violator_songs_dict['Policy of Truth']
z = violator_songs_dict['Blue Dress']
total2 = x + y + z
print('А другие три песни звучат', round(total2, 2), 'минут')