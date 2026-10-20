print('Номер 19')
import re
pat=r"(?:\+7|8) (?:\d{3}|\(\d{3}\)) \d{3}-\d{2}-\d{2}"
with open('19.txt','r',encoding='utf-8') as file:
    num=re.findall(pat,file.read())
    for i in num:
        print(i)