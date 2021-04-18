"""
Программа фильтрации показаний тензометрического датчика.
В файде записана построчно функция y(x) в ыиде "значение Y / значение х"
Необходимо считать с файла данные и записать в отдельные массивы значения x и y.
Затем сделать преобразования с значениями и записать результат в файл.

"""



class InputData:
    """
    Определяем глобальный класс данных
    """
    def __init__(self, data):
        self.data = list(data)



    @staticmethod
    def input_data_file():
        """
        Импортируем данные из файла и записываем в массив
        """
        data = []
        file_name = 'input_data'
        with open(file_name) as f:
            for i in f:
                data.append(i)
            yield data


    def tranformation_data(self):
        """
        Разделяем данные на два массива
        """
        x = []
        y = []
        for i in self.data:
            for j in i:
                data = j.split('/')
                x.append(float(data[1]))
                y.append(float(data[0]))
        return y, x


class FilterData(InputData):
    """
    Определяем дочерний класс преобразований над данными
    """
    def tranformation_data_new(self):
        """
        Фильтруем значения функции
        """
        filter_x = []
        for i in range(len(self.tranformation_data()[0])):
            item = (self.tranformation_data()[0][i] + self.tranformation_data()[0][i])/2
            filter_x.append(item)
        return filter_x

    def data_output(self):
        """
        Записываем результаты в файл
        """
        file_name = 'data_output'
        with open(file_name, 'a') as f:
            f.write('X' + '\t\t' + 'Y' + '\n\n')
            for i in range(len(self.tranformation_data()[0])):
                f.write(str(self.tranformation_data()[0][i]) + '\t\t' + str(self.tranformation_data()[1][i]) + '\n')


object1 = InputData(InputData.input_data_file())
object1.tranformation_data()


FilterData.tranformation_data_new(object1)
FilterData.data_output(object1)


