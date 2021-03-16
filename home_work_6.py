# class Human:
#     def __init__(self, name, male, age, date_of_birth, city):
#         self.name = name
#         self.male = male
#         self.age = age
#         self.date_of_birth = date_of_birth
#         self.city = city
#
#     def prith_information(self):
#         print(self.name)
#         print(self.male)
#         print(self.age)
#         print(self.date_of_birth)
#         print(self.city)
#
# human1 = Human('dsfdg', 'male', 25, '18-02-2005', 'fdgfd')
#
# human1.prith_information()

# class Calc:
#     def __init__(self, param1, param2, operation):
#         self.param1 = param1
#         self.param2 = param2
#         self.operation = operation
#
#     def sum(self):
#         return self.param1 + self.param2
#
#     def subt(self):
#         return self.param1 - self.param2
#
#     def multiply(self):
#         return self.param1 * self.param2
#
#     def division(self):
#         return self.param1 / self.param2
#
#     def result(self):
#         if self.operation == '+':
#             return self.sum()
#         elif self.operation == '-':
#             return self.subt()
#         elif self.operation == '*':
#            return self.multiply()
#         elif self.operation == '/':
#            return self.division()
#
# culc = Calc(int(input()), int(input()), input())
#
#
# print(culc.result())

# class Notebook:
#     notebook = []
#     def __init__(self, name, male, age, phone):
#         self.name = name
#         self.male = male
#         self.age = age
#         self.phone = phone
#
#     def add_in_notebook(self):
#         self.person = {'name' : self.name, 'male' : self.male, 'age' : self.age, 'phone' : self.phone}
#         return self.person
#
#     def check(self):
#         if Notebook.notebook:
#             for i in Notebook.notebook:
#                 if self.name not in i.get('name') and self.age not in i.get('age'):
#                     Notebook.notebook.append(self.add_in_notebook())
#         else:
#             Notebook.notebook.append(self.add_in_notebook())
#         return Notebook.notebook
#
# notebook1 = Notebook('fdgfdg', 'dfdfg', '25', '465465')
# notebook2 = Notebook('yjnb', 'dfd', '30', '6644660')
# notebook1.check()
# notebook2.check()
# print(Notebook.notebook)


class Notebook:
    new_notebook = {}
    def __init__(self, name, age, phone, city):
        self.name = name
        self.age = age
        self.phone = phone
        self.city = city

    def ID(self):
        key_random = self.name[0] + self.age + self.phone[::2] + self.city[-1]
        ID = 'ID' + str(key_random)
        return ID
    def add_person(self):
        self.person = {'name' : self.name, 'age' : self.age, 'phone' : self.phone, 'city' : self.city}
        return self.person
    def check(self):
        n = {self.ID(): self.add_person()}
        if self.ID not in Notebook.new_notebook:
            Notebook.new_notebook.update(n)
        else:
            Notebook.new_notebook.update(n)
        return Notebook.new_notebook


person1 = Notebook('Jack', '23', '+3806545260012', 'Dnipro')

person2 = Notebook('Nick', '30', '+8452124545', 'Lviv')
person1.check()
person2.check()
print(Notebook.new_notebook)