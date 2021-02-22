# year = int(input())
# age = 2021 - year
# if  age >= 18:
#     name = input ('Enter your name: ')
#     print(name + ' ' + str(age))
# a = [1,2,3,4,5,6,7,8,9]
#
#
# a1 = a[1::2]
# print(sum(a1))
a = int(input())

b=1
# for i in range(1,a):
#     b = b*i
while b>0:
    b *= a
    a -= 1
print(b)