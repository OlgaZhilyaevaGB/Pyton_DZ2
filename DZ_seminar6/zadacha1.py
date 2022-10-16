#Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#Пример:
#пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# from re import X

# Num = int(input('Введите число: '))

# fact = 1
# for i in range(Num):
#     i = i + 1
#     fact *= i
# #     print(fact, end = ' ')

from math import factorial

Num = int(input('Введите число: '))
f = lambda x: ((x == 1) and 1) or x * factorial(x -1)
fact = list( f(i) for i in range(1, Num +1))
print(fact)
