"""
1. Вычислить число c заданной точностью d
Пример:
- при d = 0.001, π = 3.141    10^{-1} ≤ d ≤10^{-10}
    3,1415926535
2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной
последовательности.

Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

Пример:

- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
"""
#Задача №1
# import math
#
# d = list(input('Enter d=: ').split('.'))
# capacity = sum(map(lambda x: x.isdigit(), d[1]))
# print(capacity)
# n = 1
# result = 0
#
# for i in range(capacity * 200000):
#     if i % 2 == 0:
#         result += 4 / n
#     else:
#         result -= 4 / n
#     n += 2
# print('Вычисление по ряду Лейбница:   ', round(result, capacity))
# print('Использование библиотеки math: ', round(math.pi, capacity))

#Задача №2
# n = int(input('Enter number: '))
# i = 2
# result = []
# while i * i <= n:
#     while n % i == 0:
#         result.append(i)
#         n = n / i
#     i = i + 1
# if n > 1:
#     result.append(int(n))
# print(result)

data = list(map(int, input().split()))
print('Source list                  ', data)
print('List with unique elements    ', list(set(data)))
