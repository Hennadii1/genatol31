from ftplib import FTP
import threading
import random
import time

class FTPdownload:
    def __init__(self, adress):
        self.adress = adress
        self.ftp = FTP(self.adress)
        self.ftp.login()


    def direcrory(self, dicectory):
        self.direcrory = dicectory
        self.ftp.cwd(dicectory)
        data = self.ftp.nlst()
        return data

    def filter_file(self,files):
        data_file = []
        for i in files:
            if i.count('.'):
                data_file.append(i)
        return data_file

    def download(self, data):
        sleep = random.randrange(1, 2)
        time.sleep(sleep)
        for i in range(len(data)):
            with open(data[i], 'wb') as fp:
                self.ftp.retrbinary('RETR ' + data[i], fp.write)
            print(i)
        self.ftp.quit()


adress = FTPdownload('ftp.us.debian.org')
n = adress.direcrory('debian')

print(n)
m = adress.filter_file(n)
print(m)
b = adress.download(m)
for i in m:
    t = threading.Thread(target= b, args=(i,))
    t.start()

