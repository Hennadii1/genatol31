import os
# name = input()
# def serch(n):
#     some_dict = {}
#     cont = 0
#     if n in os.listdir():
#         for i in os.listdir(n):
#             a1 = i.split('.')
#             a2 = a1[1]
#             if a2 in i:
#                 cont = cont + 1
#             a = {a2: cont}
#             some_dict.update(a)
#         print(some_dict)
#
#     else:
#         print('No')
# serch(name)

# way = input()
# name = input()
#
# def coint_file (n, m):
#     file_list = []
#     for i in os.listdir(n):
#         a = i.split('.')
#
#         if a[1] == m:
#             file_list.append(i)
#     print(file_list)
# coint_file(way, name)

way = input()
def func(n):

    for i in os.listdir(n):
        a = i.split('.')
        if a[1] not in os.listdir(n):
            os.mkdir(a[1])
        elif i.endswith(a[1]):
            os.replace(i, n + a[1])

func(way)