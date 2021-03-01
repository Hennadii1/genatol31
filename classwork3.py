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
# if b <= diametr:
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

