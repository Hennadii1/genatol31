class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def get_info(self):
        return (self.name + ' ' + self.surname + ', ' + str(self.age) + ' years')

class Student(Person):

    def __init__(self, name, surname, age, date_of_birth):
        Person.__init__(self, name, surname,age)
        self.date_of_birth = date_of_birth

    def get_info(self):
        return (Person.get_info(self) + ', ' + str(self.date_of_birth))

class Class:
    def __init__(self, classname, list_student):
        self.classname = classname
        self.list_student = list_student

    def get_class(self):
        print(self.classname)
        print(self.list_student)

class Teacher(Person):


s1 = Student('Ivan', 'Ivanov', 14, 2005)
s2 = Student('Ivan', 'Ivanov', 14, 2005)
list_student = ['s1','s2']
s1.get_info()
print(s1.get_info())

class1 = Class('9B' , list_student)
class1.get_class()