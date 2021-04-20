class Person:
    person_dict = {}

    def __init__(self, user_name, user_phone):
        self.user_name = user_name
        self.user_phone = user_phone
        self.user_id = 10000


    def post(self):
        create_id = self.user_id + 1
        create_person_data = [self.user_name, self.user_phone]
        if not Person.person_dict.get(create_id):
            person_data = {create_id : create_person_data}
            Person.person_dict.update(person_data)
        else:
            id = int(list(Person.person_dict)[-1]) + 1
            person_data = {id : create_person_data}
            Person.person_dict.update(person_data)
        return Person.person_dict


    def delete(self, id):
        if Person.person_dict.get(id):
            del Person.person_dict[id]
            return Person.person_dict
        else:
            print('Person is not found!')


    def put(self, id, name, phone):
        if Person.person_dict.get(id):
            put_person = {id : [name, phone]}
            Person.person_dict.update(put_person)
            return Person.person_dict
        else:
            print('Person is not found!')


    def get(self):
        for i in Person.person_dict:
            print(str(i) + ' - ' + ' ' + str(Person.person_dict.get(i)[0]) + ' - ' + ' ' + str(Person.person_dict.get(i)[1]))


person1 = Person('Ivan' , '+54156416541')
person2 = Person('Vovan' , '+54156416541')
person3 = Person('Stepan' , '+54156416541')
person4 = Person('Bratan' , '+54156416541')
person1.post()
person2.post()
person3.post()
person4.post()
# person3.delete(10003)
person5 = Person('Roman', '+542113')
person5.post()
person1.get()

print(Person.person_dict)
