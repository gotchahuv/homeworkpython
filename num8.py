print('номер 8')
def file_read(file):
    try:
        with open(file, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print('Файла нет')
    except PermissionError:
        print('Нет прав')
    except UnicodeDecodeError:
        print('Декордировать файл не получилось')
    except OSError:
        print('Ошибка операционный системы')

a=file_read("")
print(a)