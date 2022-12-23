#Задайте число. Составьте список чисел Фибоначчи, в том числе 
# для отрицательных индексов.
#Пример:
#для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи
print('Программа для поиска числа N   фибоначчи ')
numFibo = int(input('Введите число для расчета его фибоначчи: '))
fiboNum = []
fiboNumRevers = []
for i in range(0, numFibo +1 ):
    if i == 0:
        fiboNum.append(0)
    if i == 1 or i == 2:
        fiboNum.append(1)
    if i > 2:
        fiboNum.append(fiboNum[i-2]+fiboNum[i-1])

for i in range(numFibo):
    if i == 0:
        fiboNumRevers.append(1)
    if i == 1:
        fiboNumRevers.append(-1) 
    if i >=2:
        fiboNumRevers.append(fiboNumRevers[i-2] - fiboNumRevers[i - 1] )
fiboNumRevers.reverse() 

my_finish_nega_fibo = fiboNumRevers + fiboNum  
print(my_finish_nega_fibo)    