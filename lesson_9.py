class Drob:

    def __init__(self, chislitel, znamenatel, celoe=0):
        self.celoe = celoe
        self.chislitel = chislitel
        self.znamenatel = znamenatel

    def preobrazovatel(self):
        if self.chislitel > self.znamenatel:
            self.celoe = self.celoe + self.chislitel // self.znamenatel
            self.chislitel = self.chislitel % self.znamenatel

        return self.chislitel, self.celoe

    def sum_drob(self, new_drob):
        sum_celoe = self.celoe + new_drob.celoe
        sum_znamenatel = self.znamenatel * new_drob.znamenatel
        sum_chislitel = self.chislitel*new_drob.znamenatel + new_drob.chislitel*self.znamenatel
        self.chislitel = sum_chislitel
        self.celoe = sum_celoe
        self.znamenatel = sum_znamenatel
        self.chislitel, self.celoe = self.preobrazovatel()




        return (str(self.celoe) + ' ' + str(self.chislitel) + '/' + str(self.znamenatel))

    def subt_drob(self, new_drob1):
        subt_celoe = self.celoe - new_drob1.celoe
        subt_znamenatel = self.znamenatel * new_drob1.znamenatel
        subt_chislitel = self.chislitel*new_drob1.znamenatel - new_drob1.chislitel*self.znamenatel
        self.chislitel = subt_chislitel
        self.celoe = subt_celoe
        self.znamenatel = subt_znamenatel
        self.chislitel, self.celoe = self.preobrazovatel()

        return (str(subt_celoe) + ' ' + str(subt_chislitel) + '/' + str(subt_znamenatel))


drob_1 = Drob(1,4,3)
drob_2 = Drob(2,3,2)
drob_1.preobrazovatel()
drob_2.preobrazovatel()
print(Drob.sum_drob(drob_1,drob_2))
print(Drob.subt_drob(drob_1,drob_2))