from ftplib import FTP
import threading
# ftp = FTP('ftp.us.debian.org')
# ftp.login()
#
# ftp.cwd('debian')
# data = ftp.nlst()
# print(data)
# ftp.quit()

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

        for i in data:
            with open(i, 'wb') as fp:
                t = threading.Thread(target = self.ftp.retrbinary, args= ('RETR ' + i, fp.write),)
                t.start()
        self.ftp.quit()


adress = FTPdownload('ftp.us.debian.org')
n = adress.direcrory('debian')

print(n)
m = adress.filter_file(n)
print(m)
adress.download(m)
