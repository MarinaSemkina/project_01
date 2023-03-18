# Задача 1.2.

# Пункт A. 
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут
import datetime
import random

my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]

g = random.choices(my_favorite_songs, k = 3)
sum = g[0][1] + g[1][1] + g[2][1]
min = int(sum)
sec = (sum - min) * 100

if sec > 60:
    sec = sec - 60
    min += 1
time = datetime.time(0, min, int(round(sec, 2)) )
print(f"Три песни {g[0]}, {g[1]}, {g[2]}, звучат {time}" )



# Пункт B. 
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.

my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}

z = list(my_favorite_songs_dict.values())
n, p, l = random.choices(z, k = 3)
sum2 = n + p + l

min2 = int(sum2)
sec2 = (sum2 - min2) * 100

if sec2 > 60:
    sec2 = sec2 - 60
    min2 += 1
time = datetime.time(0, min2, int(round(sec2, 2)) )
print(f"Три песни звучат {time}" )

# Дополнительно для пунктов A и B
# Пункт C.
# Сгенерируйте случайные песни с помощью модуля random
# import random

# Дополнительно 
# Пункт D.
# Переведите минуты и секунды в формат времени. Используйте модуль datetime 