class RangeIter:
    def __init__(self, end, begin=0, step=1):
        self.end = end
        self.begin = begin
        self.step = step
        self.counter = self.begin

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.end:

            self.counter = self.counter + self.step
            return self.counter
        else:
            raise StopIteration

n = RangeIter(10,1,2)
# for i in n:
#     print(i)


def range_generator(end, begin=0, step=1):
    counter = begin
    while counter < end:
        counter = counter + step
        yield counter


n_gen = range_generator(10,1,2)

# for i in n_gen:
#     print(i)




class Weather:
    def __init__(self, time):
        self.time = time
        self.counter = 0

    @staticmethod
    def read_file():
        file_weather = open('weather')
        lines = [i for i in file_weather]
        return lines

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < len(Weather.read_file()):
            n = self.counter
            line = Weather.read_file()
            self.counter = self.counter + 1
            return line[n]
        else:
            raise StopIteration

    def get_weather(self):
        line = next(self).split('/')
        while not line[0] == self.time:

            line = next(self).split('/')
        return line

    def weather_output(self):
        print(self.get_weather())




weather = Weather('4.00')

weather.weather_output()
