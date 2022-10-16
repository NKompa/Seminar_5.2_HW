# Реализуйте алгоритм перемешивания списка.

import random

list_lenght = int(input('Введите количество элементов в списке: '))
list = []
for i in range(list_lenght):
    list.append(random.randint(-50,50))
print(f'Список начальный: {list}')

list2 = sorted(list)
print(f'Список отсортированный: {list2}')

list3 = []
for i in range(1,list_lenght+1):
    list3.append(list[-i])
print(f'Список перевёрнутый: {list3}')