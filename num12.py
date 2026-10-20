print('номер 12')
import re
with open('12ex.txt',encoding='utf-8') as file:
   a=file.read()
emails=re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9]+\.[A-Za-z0-9]{2,}",a)
emails1=[]
for email in emails:
   if email not in emails1:
      emails1.append(email)
for i in emails1:
   print(i)