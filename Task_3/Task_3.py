# Реализуйте алгоритм перемешивания списка. Встроенный алгоритм SHUFFLE не использовать! Реализовать свой метод

import random

l= int(input("Пожалуйста введите количество элементов списка:"))

my_list=[]
for i in range(1,l+1):
    n=random.randint(1,10)
    my_list.append(n)
    print(n, end=" ")
print()
print(my_list)

for i in range(len(my_list)):
    r=random.randint(0,(len(my_list)-1))
    my_list[i], my_list[r]= my_list[r], my_list[i]
print(my_list)