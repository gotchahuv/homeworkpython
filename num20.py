print('Номер 20')
import re
pat=r'\d{2}\.\d{2}\.\d{4}'
with open('20.txt','r',encoding='utf-8') as file:
    print(re.findall(pat,file.read()))