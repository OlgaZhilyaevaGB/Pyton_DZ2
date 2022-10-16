#Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму

# num = int(input("Введите число N: "))
# s = 0
# for i in range(1,num+1):
#     s += (1+1/i)**i
# print(f"Cумма последовательности (1+1/n)^n равна {round(s,2)}")

num = int(input("Введите число N: "))
s=list(range(1,num+1))
li=(list(map(lambda i:(1+1/i)**i,s)))
print(f"Cумма последовательности (1+1/n)^n равна {round(sum(li),2)}")

