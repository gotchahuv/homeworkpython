print('Номер 24')
import re
products = ["PRD-12345","PRD-00123","USR-12345","PRD-987","PRD-ABCDE","PRD-54321"]
pat=r'PRD-[0-9]{5}'
for i in products:
    if re.fullmatch(pat,i):
        print(i)