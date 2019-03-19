import csv
import datetime
import os


class Logger:
    def __init__(self, filename):
        self.filename = filename
        self.dt = str(datetime.datetime.now().strftime('_%Y%m%d%H_%M_%S'))
        self.path = 'C:\\Users\\Joniu\\Documents\\STUDIA\\Semestr_VI\\Sztuczna_Inteligencja\\TTP\\'
        self.file = None

    def create_file(self):
        self.path += self.filename
        os.makedirs(self.path, exist_ok=True)
        self.file = self.filename + self.dt + '.csv'
        with open(os.path.join(self.path, self.file), mode='+x') as log_file:
            # fields = ['generation number', 'best', 'average', 'worst']
            csv.writer(log_file, delimiter=';')

    def write(self, row):
        with open(os.path.join(self.path, self.file), mode='a', newline='') as log_file:
            # fields = ['generation number', 'best', 'average', 'worst']
            writer = csv.writer(log_file, delimiter=';')
            writer.writerow(row)
