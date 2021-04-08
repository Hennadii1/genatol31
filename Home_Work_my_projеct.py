# Задача: программа предваительного расчета стоимости кухни.
# пользовтеля просят пошагово вести некоторые данные:
# 1. Контактные данные, которые являются приватными (имя, номер тедефона, e_mail).
# 2. Тип кухни (прмая или угловая).
# 3. Длину кухни (если прямая - 1 длина, если угловая - 2 длины).
# 4. Тип фурниуры (бюжетная, цена/качество, брендовая).
# 5. Тип фасада (обычный, крашенные, массив дерева).
# Есть фиксирваная цена за 1 м/п кухни, тип фурнитуры и тип фасада влияют на цену путем добавления коэффициента увеличения цены.
# При этом бюджетная фурнитура и обычный фасад имеют коээф. 1.

class Kitchen:

    def __init__(self, name, phone, e_mail, kitchen_type, fittings_type, facade_type):
        self.__name = name
        self.__phone = phone
        self.__e_mail = e_mail
        self.kitchen_type = kitchen_type
        self.fittings_type = fittings_type
        self.facade_type = facade_type

    def personal_data_input(self):
        self.__name = input('Введите Ваше имя: ')
        self.__phone = input('Введите Ваш номер телефона: ')
        self.__e_mail = input('Введите Ваш адрес электронной почты: ')
        return self.__name, self.__phone, self.__e_mail

    def kitchen_data_input(self):
        self.kitchen_type = input('Введите тип кухни: 1 - прямая, 2 - угловая ...-')
        self.fittings_type = input('Введите тип фурнитуры: 1 - бюджет, 2 - цена/качество, 3 - бренд ...-')
        self.facade_type = input('Введите тип фасада: 1 - обычные, 2 - крашеные, 3 - дерево ...-')
        return self.kitchen_type, self.fittings_type, self.facade_type
