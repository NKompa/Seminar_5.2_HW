# Программа принимает на вход вещественное число и показывает сумму его цифр: 6782 -> 23; 0,56 -> 11

num = input('Введите число: ')
# 1 вариант удаления знаков
for i in ['-', '.', ',']:
    if i in num:
        num = num.replace(i, "")

# 2 вариант удаления знаков
# num = num.translate({ord(i): None for i in '-.,'})

sum = 0
for i in num:
    sum = sum + int(i)
print(sum)
