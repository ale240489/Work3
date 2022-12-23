#Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#Пример:
#[2, 3, 4, 5, 6] => [12, 15, 16];
#[2, 3, 5, 6] => [12, 15]

my_list = [2, 3,3, 5, 6]
lastIndex = len(my_list) - 1
productNums = 0
if len(my_list)%2 != 0:
    for i in range(int(len(my_list)/2)+1):
        productNums = my_list[i] * my_list[lastIndex]
        lastIndex-= 1
        print(productNums)
else:
    for i in range(int(len(my_list)/2)):
        productNums = my_list[i] * my_list[lastIndex]
        lastIndex-= 1
        print(productNums)            