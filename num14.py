from contextlib import contextmanager
@contextmanager
def log_operation(operation, processing):
    with open('1234.txt',"a",encoding='utf-8') as file:
        file.write(f'Start:{processing}\n')

        try:
            yield
        except Exception:
            file.write(f'ERROR:{processing}\n')
            raise
        else:
            file.write(f'END:{processing}\n')
with log_operation('operatiom.log','Data.processing'):
    print('Обработка данных')
with open('1234.txt','r',encoding='utf-8') as file123:
    for i in file123:
        print(i)