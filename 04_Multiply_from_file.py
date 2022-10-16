# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

import random

num = int(input('Введите количество элементов: '))
list_num = []
index = set()
for i in range(num):
    list_num.append(random.randint(-num, num+1))        # составляем список случайных чисел в количестве num
    index.add(abs(list_num[i]))                         # из это списка составляем множество для использования в качестве индекса
print(f'Список из {num} элементов: {list_num}')

file = open('file.txt', 'w')                            # записываем множество в файл
for i in index:
    if i < num:
        file.write(str(i))
        file.write('\n')
file.close()

mult = 1
file = open('file.txt','r')                             # забираем индексы из файла и перемножаем элементы с этими индексами
for i in (file):
    mult*=list_num[int(i)]
    print(f'Индекс: {i}', end='')
print(f'Произведение элементов: {mult}')
file.close()