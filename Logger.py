import csv
import os


class Logger:
    def __init__(self, filename, header):
        self.filename = filename
        self.header = header
        self.path = 'C:\\Users\\Joniu\\Documents\\STUDIA\\Semestr_VI\\Sztuczna_Inteligencja\\TTP\\'
        self.file = None

    def create_file(self):
        self.path += self.filename
        os.makedirs(self.path, exist_ok=True)
        self.file = self.filename + self.header + '.csv'
        with open(os.path.join(self.path, self.file), mode='+w') as log_file:
            csv.writer(log_file, delimiter=';')

    def write(self, row):
        with open(os.path.join(self.path, self.file), mode='a', newline='') as log_file:
            writer = csv.writer(log_file, delimiter=';')
            writer.writerow(row)
