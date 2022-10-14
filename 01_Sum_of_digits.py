# Программа принимает на вход вещественное число и показывает сумму его цифр: 6782 -> 23; 0,56 -> 11

num = input('Введите число: ')
num = num.replace('-', '')
num = num.replace('.', '')
num = num.replace(',', '')
list1 = list(num)

sum = 0
for i in num:
    sum = sum + int(i)
print(sum)