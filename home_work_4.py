# test 1

# n = [1,2,3,4,5,1]
# def sum(x):
#     if x == []:
#         return 0
#     else:
#         return x[0] + sum(x[1:])
# print(sum(n))

# test 2
#
# n = [1,2,3,4,5]
# m = [6,7,8,9,10]
# def sum(x,y):
#     b  = []
#     for i in range(len(x)):
#         b.append(x[i])
#         b.append(y[i])
#     return b
# print(sum(n,m))


# test 3

# n = int(input())
# m = int(input())
# k = int(input())
# def proverka(a, b, c):
#     if a+b > c and a+c > b and b+c > a:
#         return 'True'
#     else:
#         return 'False'
# print(proverka(n,m,k))

# test 5

# a1 = int(input('a1: '))
# b1 = int(input('b1: '))
# c1 = int(input('c1: '))
# n = int(input('n: '))
# a = list(range(a1 , a1 + n))
# b = list(range(b1 , b1 + n))
# c = list(range(c1 , c1 + n))
# def func(a, b, c):
#     for i in range(len(a)):
#         if (b[i]*b[i]  - 4*a[i]*c[i]) > 0:
#             return (str(a[i]) + 'x^2' + '+' + str(b[i]) + '+' + str(c[i]))
#
# print(func(a,b,c))

# test 6

# n = int(input())
# def func(a):
#     m = []
#     for i in range(a-1):
#         m.append(input().replace('?', '*'))
#     return m
#
# print(func(n))
# test 7

# date = input()
# new_date = date.split('-')
# def date(new):
#
#     return (new[2] + '/' + new[1] + '/' + new[0])
# print(date(new_date))

# test 8

# gramm = int(input())
# def mass(n):
#     kg = n/ 1000
#     t = kg / 1000
#     print(kg)
#     print(t)
# mass(gramm)

# test 9

# a = int(input())
# b = int(input())
# c = int(input())
#
# m = int(input())
# k = int(input())
# def func(*args):
#     if a < m or a < k and b < k or b < m:
#         print('True')
#     elif a < m or a < k and c < m or c < k:
#         print('True')
#     elif b < m or b < k and c < m or c < k:
#         print('True')
#     else:
#         print('False')
# func(a,b,c,m,k)

# test 10
#
# diametr = int(input())
# storona = int(input())
# def func(n,m):
#     b = 2 * m
#     if b <= n**2:
#         print('Mogno')
#     else:
#         print('Nelzya')
# func(diametr, storona)

# test 13
# n = int(input())
# def func(a):
#     i = 1
#     while i < a-1:
#         i += 1
#         if a%i == 0:
#             return 'False'
#
# print(func(n))

# 14. Вывести таблицу умножения числа M в диапазоне от числа a до числа b.
# Числа M, a и b вводит пользователь.

# M = int(input())
# a = int(input())
# b = int(input())
#
# def func(*args):
#     for i in range(a, b+1):
#         c = M * i
#         print (str(M) + ' * ' + str(i) + ' = ' + str(c))
# print(func(M,a,b))

# 11. Дан номер места в плацкартном вагоне. Определить, какое это место:
# верхнее или нижнее, в купе или боковое.

# mesto = int(input('Введите место: '))
# def func(mesto):
#     if mesto > 54:
#         print('Такого места быть не может')
#     elif mesto > 36:
#         print('У Вас боковое место')
#     elif mesto % 2 == 0:
#         print('У Вас верхнее место')
#     else:
#         print('У Вас нижнее место')
# func(mesto)

# 15. Дан одномерный массив числовых значений, насчитывающий N
# элементов. Поменять местами элементы, стоящие на чётных и нечётных
# местах: A[1] ↔ A[2]; A[3] ↔ A[4] ...

# N = int(input())
# A = list(range(1, N+1))
#
# def func(a):
#     for i in range(len(a)-1):
#         a[i], a[i+1] = a[i+1], a[i]
#     return a
# print(func(A))

# 16. Вывести список простых чисел в диапазоне d. Диапазон d вводит
# пользователь.


# d = int ( input ("Введите диапазон: "))
# def func(k):
#     print ("1")
#     print ("2")
#     for n in range (3, k):
#         for a in range (2, n):
#             if (n % a) == 0:
#                 break
#             else:
#                 print (n)
#                 break
# func(d)

# 4. Расстояние между точками. На вход поступает два значение (кортежа) с
# координатами - широта и долгота.
# Найти расстояние между этими точками. cos(d) = sin(φА)·sin(φB) +
# cos(φА)·cos(φB)·cos(λА − λB), где φА и φB — широты, λА, λB — долготы
# данных пунктов, d — расстояние между пунктами, измеряется в
# радианах длиной дуги большого круга земного шара. Расстояние между
# пунктами, измеряемое в километрах, определяется по формуле: L = d·R,
# где R = 6371 км — средний радиус земного шара.
#
# import math
#
# fA = math.radians(int(input()))
# fB = math.radians(int(input()))
# f1 = []
# f1.append(fA)
# f1.append(fB)
# f = tuple(f1)
# lA = math.radians(int(input()))
# lB = math.radians(int(input()))
# l1 = []
# l1.append(lA)
# l1.append(lB)
# l = tuple(l1)
# def func(a, b):
#     cos_d = math.sin(a[0]) * math.sin(a[1]) + math.cos(a[0]) * math.cos(a[1]) * math.cos(b[0] - b[1])
#     d = math.acos(math.cos(cos_d))
#     L = d * 6371
#     return L
# print(func(f, l))
# 12. Известна денежная сумма. Разменять её купюрами 500, 100, 10 и
# монетой 2 грн., если это возможно.

# a = int(input())
# def func(a):
#     b = a // 500
#     b1 = a % 500
#     c = b1 // 100
#     c1 = b1 % 100
#     d = c1 // 10
#     d1 = c1 % 10
#     e = d1 // 2
#     e1 = d1 % 2
#     print(str(b) + ' - ' + '500')
#     print(str(c) + ' - ' + '100')
#     print(str(d) + ' - ' + '10')
#     print(str(e) + ' - ' + '2')
#     print(str(e1) + ' остаток')
# func(a)
