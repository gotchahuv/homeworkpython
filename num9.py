import re
print('номер 9')
value=input('Введите число\n')
def parse_number(value):
    try:
        return float(value)
    except ValueError:
        if not(re.search(r"\d+",value)):
            print('В строке нет чисел')
        raise ValueError("Некорректное число")

try:
    a=parse_number(value)
    print("Число", a)
except ValueError:
    print('ОШИБКА')