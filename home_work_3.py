# test 1
#
# n = [1,2,3,4,5]
# sum = 0


# for
# for i in n:
#     sum = sum + i

# while
# i = 0
# while i < len(n):
#     sum = sum + n[i]
#     i += 1
# print(sum)

# test 2
#
# n = [1,2,3,4,5]
# m = [6,7,8,9,10]
#
# b = []
# for i in range(len(n) ):
#     b.append(n[i])
#     b.append(m[i])
# print(b)

# test 3

# a = int(input())
# b = int(input())
# c = int(input())
#
# if a+b > c and a+c > b and b+c > a and a,b,c != 0:
#     print('True')
# else:
#     print('False')

# test 5

# a1 = int(input('a1: '))
# b1 = int(input('b1: '))
# c1 = int(input('c1: '))
# n = int(input('n: '))
# a = list(range(a1 , a1 + n))
# b = list(range(b1 , b1 + n))
# c = list(range(c1 , c1 + n))
#
# for i in range(len(a)):
#
#     if (b[i]*b[i]  - 4*a[i]*c[i]) > 0:
#         print(str(a[i]) + 'x^2' + '+' + str(b[i]) + '+' + str(c[i]))


# test 6

# n = int(input())
# m = []
# for i in range(n-1):
#     m.append(input().replace('?', '*'))
# print(m)

# test 7

# date = input()
# new_date = date.split('-')
# print(new_date[2] + '/' + new_date[1] + '/' + new_date[0])

# test 8

# gramm = int(input())
#
# kg = gramm / 1000
# t = kg / 1000
# print(kg)
# print(t)

# test 9

# a = int(input())
# b = int(input())
# c = int(input())
#
# m = int(input())
# k = int(input())
#
# if a < m or a < k and b < k or b < m:
#     print('True')
# elif a < m or a < k and c < m or c < k:
#     print('True')
# elif b < m or b < k and c < m or c < k:
#     print('True')
# else:
#     print('False')

# test 10
#
# diametr = int(input())
# storona = int(input())
# b = 2 * storona
# if b <= diametr**2:
#     print('Mogno')
# else:
#     print('Nelzya')

# test 13
# n = int(input())
# i = 1
# while i < n-1:
#     i += 1
#     if n%i == 0:
#         print('False')
#         break
# 14. Вывести таблицу умножения числа M в диапазоне от числа a до числа b.
# Числа M, a и b вводит пользователь.

# M = int(input())
# a = int(input())
# b = int(input())
#
#
# for i in range(a, b+1):
#     c = M * i
#     print(str(M) + ' * ' + str(i) + ' = ' + str(c))

# 11. Дан номер места в плацкартном вагоне. Определить, какое это место:
# верхнее или нижнее, в купе или боковое.

# mesto = int(input('Введите место: '))
#
# if mesto > 54:
#     print('Такого места быть не может')
# elif mesto > 36:
#     print('У Вас боковое место')
# elif mesto % 2 == 0:
#     print('У Вас верхнее место')
# else:
#     print('У Вас нижнее место')

# 15. Дан одномерный массив числовых значений, насчитывающий N
# элементов. Поменять местами элементы, стоящие на чётных и нечётных
# местах: A[1] ↔ A[2]; A[3] ↔ A[4] ...

# N = int(input())
# A = list(range(1, N+1))
# print(A)
#
# for i in range(len(A)-1):
#     A[i], A[i+1] = A[i+1], A[i]
# print(A)

# 16. Вывести список простых чисел в диапазоне d. Диапазон d вводит
# пользователь.


# d = int ( input ("Введите диапазон: "))
# print ("1")
# print ("2")
# for n in range (3, d):
#     for a in range (2, n):
#         if (n % a) == 0:
#             break
#         else:
#             print (n)
#             break

# 4. Расстояние между точками. На вход поступает два значение (кортежа) с
# координатами - широта и долгота.
# Найти расстояние между этими точками. cos(d) = sin(φА)·sin(φB) +
# cos(φА)·cos(φB)·cos(λА − λB), где φА и φB — широты, λА, λB — долготы
# данных пунктов, d — расстояние между пунктами, измеряется в
# радианах длиной дуги большого круга земного шара. Расстояние между
# пунктами, измеряемое в километрах, определяется по формуле: L = d·R,
# где R = 6371 км — средний радиус земного шара.

# import math
#
# fA = math.radians(int(input()))
# fB = math.radians(int(input()))
# lA = math.radians(int(input()))
# lB = math.radians(int(input()))
# R = 6371
# cos_d = math.sin(fA) * math.sin(fB) + math.cos(fA) * math.cos(fB) * math.cos(lA - lB)
# d = math.acos(math.cos(cos_d))
# L = d * R
# print(L)

# 12. Известна денежная сумма. Разменять её купюрами 500, 100, 10 и
# монетой 2 грн., если это возможно.

# a = int(input())
# b = a // 500
# b1 = a % 500
# c = b1 // 100
# c1 = b1 % 100
# d = c1 // 10
# d1 = c1 % 10
# e = d1 // 2
# e1 = d1 % 2
# print(str(b) + ' - ' + '500')
# print(str(c) + ' - ' + '100')
# print(str(d) + ' - ' + '10')
# print(str(e) + ' - ' + '2')
# print(str(e1) + ' остаток')
