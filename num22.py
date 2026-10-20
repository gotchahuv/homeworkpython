print('Номер 22')
import re
pat=r"https?://[^\s,]+"
a='Полезные сайты: https://python.org, http://example.com/page,https://example.com/docs/index.html и ftp://files.example.com/data.'
num=re.findall(pat,a)
for i in num:
    print(i)