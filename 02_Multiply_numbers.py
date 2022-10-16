# Программа принимает на вход число N и выдает набор произведений чисел от 1 до N: пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

number = abs(int(input('Введите целое число: ')))
mult = 1
list = []
for i in range(1,number+1):
    mult *=i
    list.append(mult)
print(list)