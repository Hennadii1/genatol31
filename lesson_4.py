# some_list = [1, 2, 3, 5, 5, 5, 4, 8, 84, 4, 5, 4, 5]
#
# def func(a):
#     b = 0
#     c = 0
#     for i in a:
#         if i % 2 == 0:
#             b = b + 1
#         else:
#             c = c + 1
#     return b, c
#
#
# print(func(some_list))

# num = int(input())
# def fibonachi(n):
#     if n <= 1:
#         return n
#     else:
#         return (fibonachi(n-1) + fibonachi(n-2))
#
# for i in range(num):
#     print(fibonachi(i))


# some_string = 'sdfdgfdgfdgfdgfdg'
#
# def reverse(a):
#
#     return a[::-1]
# print(reverse(some_string))

# a = [1,2,3,4,5]
# b = [6,7,8,9,10]
#
# def sum(x , y):
#     c = []
#     if len(x) == len(y):
#         for i in range(len(x)):
#             n1 = x[i] + y[i]
#             c.append(n1)
#         return c
#     else:
#         return 'no'
#
# print(sum(a,b))

# name = input()
# age = input()
# city = input()
# phone = input()
# def some_dict(a , b , c, d):
#
#     return {'name':a, 'age':b, 'city':c, 'phone':d}
# print(some_dict(name,age,city,phone))

# some_list = [1,656,79,654,85,4,6,789,5,41,4,4,231,50,20]
# def new_list(n):
#     a = []
#     b = []
#     c = []
#     for i in n:
#         if i % 2 == 0:
#             a.append(i)
#         elif i % 3 == 0:
#             b.append(i)
#         elif i % 5 == 0:
#             c.append(i)
#     return a, b, c
# print(new_list(some_list))

# a = float(input())
# b = float(input())
# operation = input()
# def calc(n,m):
#     if operation == '+':
#         return n+m
#     elif operation == '-':
#         return n-m
#     elif operation == '*':
#         return n*m
#     elif operation == '/':
#         return n/m
# print(calc(a,b))

# some_list = [1,2,3,[1,2,3,5],'fdgf','fdgfdg', {'a':3, 'c':56}, {'1':1, '2':2}]
# def new_list(n):
#     a = []
#     b = []
#     c = []
#     for i in n:
#         if isinstance(i,int):
#             a.append(i)
#         elif isinstance(i,list):
#             a.extend(i)
#         elif isinstance(i, str):
#             b.append(i)
#         elif isinstance(i,dict):
#             c.append(i)
#     return a, b, c
# print(new_list(some_list))
