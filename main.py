"""
1. Вычислить число c заданной точностью d
Пример:
- при d = 0.001, π = 3.141    10^{-1} ≤ d ≤10^{-10}
    3,1415926535
2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной
последовательности.

4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
многочлена и записать в файл многочлен степени k.
Пример:
    - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

5. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
"""
import random
import re

# Задача №1
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

# Задача №2
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

# №задача №3
# data = list(map(int, input().split()))
# print('Source list                  ', data)
# print('List with unique elements    ', list(set(data)))

# Задача №4
# result = ''
# k = int(input('K= '))
# count = list(random.randint(1, 100) for x in range(0, k + 1))
#
# for item in count:
#     if item != 0:
#         tmp = str(item)
#         if k > 1:
#             tmp = tmp + 'X*' + str(k)
#         elif k == 1:
#             tmp = tmp + 'X'
#         result += tmp + '+'
#
#     k -= 1
# with open('result.txt', 'w') as f:
#     f.write(result[:-1] + '=0')
# Задача №5
# with open('01', 'r') as f1:
#     source1 = f1.read()
# with open('02', 'r') as f2:
#     source2 = f2.read()
#
# if source1[:1] != '-':
#     source1 = '+' + source1
# if source2[:1] != '-':
#     source2 = '+' + source2
#
#
# def split_pol(source):
#     result = []
#     s = source.replace(' ', '')
#     result.append(re.findall(r'\d{1,}X..\d', s))
#     some = re.findall(r'\d{1,}X[+-]', s)
#     result.append(some[0][:-1])
#     result.append(re.findall(r'[+-]\d{1,}', s))
#     return result
#
# tmp_list = []
# pow_list1 = []
# pow_list2 = []
# total = []
#
# splited_str1 = split_pol(source1)
# splited_str2 = split_pol(source2)
#
#
# for i in split_pol(source1)[0]:
#     tmp_list.append(i[-1:])
#     pow_list1.append(i[-1:])
#
# for j in split_pol(source2)[0]:
#     tmp_list.append(j[-1:])
#     pow_list2.append(j[-1:])
#
# uniq_pow = list(set(tmp_list))
#
# for el in uniq_pow:
#     if el not in pow_list1:
#         splited_str1[0].append('0X**' + el)
#         index = splited_str1[0].index('0X**' + el)
#         splited_str1[2].insert(index, '+0')
#
#
# for el in uniq_pow:
#     if el not in pow_list2:
#         splited_str2[0].append('0X**' + el)
#         index = splited_str2[0].index('0X**' + el)
#         splited_str2[2].insert(index, '+0')
#
#
# len_s1 = len(splited_str1)
# len_s2 = len(splited_str2)
#
# if len_s1 < len_s2:
#     splited_str1.insert(1, '0X')
# elif len_s1 > len_s2:
#     splited_str2.insert(1, '0X')
# if len(splited_str1[0]) < len(splited_str2[0]):
#     splited_str2[0].append()
#
# splited_str1_mod = splited_str1[0]
# splited_str1_mod.append(splited_str1[1])
#
# splited_str2_mod = splited_str2[0]
# splited_str2_mod.append(splited_str2[1])
#
# for i in splited_str1_mod:
#     for j in splited_str2_mod:
#         if i[-1:] == j[-1:]:
#             tmp = i.split('X')
#             index1 = splited_str1_mod.index(i)
#             index2 = splited_str2_mod.index(j)
#             calc = int(splited_str1[2][index1]) + int(splited_str2[2][index2])
#             res = str(calc) + 'X' + tmp[1]
#             total.append(res)
#
# odds_without_x = int(splited_str1[2].pop()) + int(splited_str2[2].pop())
# total.append(str(odds_without_x))
#
# final_result = ''
# for el in total:
#     if el[:1] != '-':
#         if el[:1] != '0':
#             final_result += el + '+'
#
#     else:
#         final_result = final_result[:-1]
#         final_result += el + '+'
#
#
# with open('result.txt', 'w') as file:
#     file.write(final_result[:-1]+'=0')