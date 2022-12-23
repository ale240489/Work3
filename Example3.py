#Задайте список из вещественных чисел. Напишите программу, которая найдёт 
# разницу между максимальным и минимальным значением дробной части элементов, 
# отличной от 0.
#Пример:
#[1.1, 1.2, 3.1, 5, 10.01] => 0.19
import random


my_list = []
for i in range(10):
    index = random.randint(0, 3)
    my_list.append(round(random.uniform(0, 10),index))    
my_listFraction = []
for i in range(len(my_list)):
    my_listFraction.append(round(my_list[i] - int(my_list[i]),3))
print(my_listFraction)   
min = my_listFraction[0]
max = my_listFraction[1]
for i in range(len(my_listFraction)):
    if my_listFraction[i] < min and my_listFraction[i] != 0:
        min = my_listFraction[i]
    elif my_listFraction[i] > max:
        max = my_listFraction[i]
print(f'Минимальное число = {min}')
print(f'Максимальное число = {max}') 
print(f'Разница между максимальным и минимальным число равна = {max - min}')         
