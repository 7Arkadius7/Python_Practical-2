# Задайте список из n чисел последовательности (1 + 1/n)^n. Вывестив консоль сам список и сумму его элементов.

n= int(input("Пожалуйста введите число:"))

my_list=[]

for i in range(1, n+1):
    my_list.append((1 + 1/i)**i)
print(my_list)
print(round((sum(my_list)),2))