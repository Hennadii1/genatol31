# class Animal:
#     def __init__(self, food, location):
#         self.food = food
#         self.location = location
#
#     def eat(self):
#         print('eat')
#
#     def sleep(self):
#         print('sleep')
#
#     def makeNoise(self):
#         print('makeNoise')
#
# class Dog(Animal):
#
#     def eat(self):
#         print('Dog eat')
#
#     def makeNoise(self):
#         print('The dog is a sleep')
#
# class Cat(Animal):
#
#     def eat(self):
#         print('Cat eat')
#
#     def makeNoise(self):
#         print('The cat is a sleep')
#
# class Horse(Animal):
#
#     def eat(self):
#         print('Horse eat')
#
#     def makeNoise(self):
#         print('The horse is a sleep')
#
# class Vet:
#     def triatAnimal(self, Animal):
#         print(Animal.food, Animal.location)
#
#
# vet = Vet()
# dog = Dog('Dogkorm', 'budka')
# cat = Cat('Catkorm', 'kovrik')
# horse = Dog('Seno', 'stoilo')
#
# vet.triatAnimal(dog)
# vet.triatAnimal(cat)
# vet.triatAnimal(horse)

import random
class SunMatrix:
    def __init__(self, element):
        self.element = element


    def createMatrix(self):
        self.matrix = []

        for i in range(self.element):
            masive = []
            self.matrix.append(masive)

            for j in range(self.element):
                masive.append(random.randint(0,100))

        return self.matrix

    def __add__(self, other):
        new_matrix = []

        if len(self.matrix) == len(other.matrix):
            for i in range(len(self.matrix)):
                new_masive = []
                new_matrix.append(new_masive)
                for j in range(len(self.matrix[0])):
                    a = self.matrix[i][j] + other.matrix[i][j]
                    new_masive.append(a)
            return new_matrix
        else:
            return 'Pleas create the same matrix!'

    def multiply(self, parametr):
        new_matrix1 = []
        for i in range(len(self.matrix)):
            new_masive1 = []
            new_matrix1.append(new_masive1)
            for j in range(len(self.matrix[0])):
                a = self.matrix[i][j] * parametr
                new_masive1.append(a)
        return new_matrix1

    def multiplyMatrix(self, otherMatrix):
        new_matrix2 = []
        for i in range(len(self.matrix)):
            new_masive2 = []
            new_matrix2.append(new_masive2)
            for j in range(len(self.matrix[0])):
                a = self.matrix[i][j] * otherMatrix.matrix[i][j]
                new_masive2.append(a)
        return new_matrix2


matrix1 = SunMatrix(3)
matrix2 = SunMatrix(3)
matrix1.createMatrix()
matrix2.createMatrix()
print(matrix1.createMatrix())
print(matrix2.createMatrix())
# print(matrix1 + matrix2)
#
# print(matrix1.multiply(2))
print(matrix1.multiplyMatrix(matrix2))