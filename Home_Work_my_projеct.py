class InputData:
    def __init__(self, data):
        self.data = list(data)



    @staticmethod
    def input_data_file():
        data = []
        file_name = 'input_data'
        with open(file_name) as f:
           for i in f:
               data.append(i)
        return data

    def tranformation_data(self):
        x = []
        y = []
        for i in InputData.input_data_file():
            data = i.split('/')
            x.append(float(data[1]))
            y.append(float(data[0]))
        return y, x


class FilterData(InputData):
    def tranformation_data(self):
        filter_x = []
        for i in range(len(self.tranformation_data()[0])-1):
            item = (self.tranformation_data()[0][i] + self.tranformation_data()[0][i+1])/2
            filter_x.append(item)
        return filter_x

    def data_output(self):
        file_name = 'data_output'
        with open(file_name, 'a') as f:
            f.write('X' + '\t\t' + 'Y' + '\n\n')
            f.write(str(self.tranformation_data()[0][0]) + '\t\t' + str(self.tranformation_data()[1][0]) + '\n')
            for i in range(len(self.tranformation_data()[0])-1):
                f.write(str(self.tranformation_data()[0][i]) + '\t\t' + str(self.tranformation_data()[1][i+1]) + '\n')




object1 = InputData(InputData.input_data_file())
filter1 = FilterData
filter1.tranformation_data(object1)
filter1.data_output(object1)

# print(object1.tranformation_data()[0])
# print(object1.tranformation_data()[1])
