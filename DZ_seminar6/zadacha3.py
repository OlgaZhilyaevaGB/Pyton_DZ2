#Задайте последовательность цифр. Напишите программу, которая выведет список неповторяющихся элементов
#исходной последовательности
#Пример:
#47756688399943 -> [5]
#1113384455229 -> [8,9]
#1115566773322 -> []

# from random import  randint as r

# num = int(input("Введите размер списка: "))
# list = []
# for i in range(1,num+1):
#    elem = r(1,5)
#    list.append(elem)
# print(list)

# list2 = {}
# rez=''
# for a in list:
#     if list2.get(a):
#        list2[a]=list2.get(a)+1
#     else:
#         list2[a]=1
# for i in list2.items():
#     if i[1]==1:
#         rez += str(i[0])

# print(f"Уникальные элементы в списке: {rez}") if rez else print("Нет уникальных элементов")


list = list(map(int, input("Введите числа через пробел:\n").split()))
print(f"Исходный список: {list}")
list2 = []
[list2.append(i) for i in list if i not in list2]
print(f"Уникальные элементы в списке: {list2}") 
