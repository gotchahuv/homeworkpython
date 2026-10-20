print('Номер 10')
import csv
from abc import ABC, abstractmethod
def log(func):
    def wrapper(self, filename):
        res=func(self, filename)
        try:
            with open('log.txt','a',encoding='utf-8') as f:
                f.write(f'{filename}: {res}\n')
        except OSError:
            print('Ошибка записи журнала')
        return res
    return wrapper
class FileProcessor(ABC):
    @log
    def process(self, filename):
        try:
            with open(filename, 'r',encoding='utf-8',newline='') as f:
                return self.analyze(f)
        except (OSError,UnicodeError,csv.Error) as e:
            return f'Ошибка: {e}'
    @abstractmethod
    def analyze(self, f):
        pass
class TextFileProcessor(FileProcessor):
    def analyze(self, f):
        lines=0
        words=0
        for line in f:
            lines+=1
            words+=len(line.split())
        return f'Строки {lines},Слова {words}'
class CSVFileProcessor(FileProcessor):
    def analyze(self, f):
        reader=csv.reader(f)
        header=next(reader, None)
        if header is None:
            return f'Записи: 0, Столбцы: 0'
        columns=len(header)
        records=0
        for row in reader:
            if len(row)==columns:
                records+=1
        return f'Записи: {records}, Столбцы: {columns}'
def run(processor, filename):
    result=processor.process(filename)
    print(result)
#Создаем текстовый файл
with open('test.txt', 'w', encoding='utf-8') as f:
    f.write('Привет мир\n')
    f.write('Как дела\n')
    f.write('Я изучаю Python\n')
with open('test.csv', 'w', encoding='utf-8') as f:
    f.write('name,age\n')
    f.write('Ivan,18\n')
    f.write('Petr,19\n')
    f.write('Anna,20\n')
with open('empty.txt', 'w') as f:
    pass
text=TextFileProcessor()
csv_file=CSVFileProcessor()
print('Текстовый файл:')
run(text, 'test.txt')
print('CSV-файл:')
run(csv_file, 'test.csv')
print('Пустой файл:')
run(text, 'empty.txt')
print('Несуществующий файл:')
run(text, 'unknown.txt')