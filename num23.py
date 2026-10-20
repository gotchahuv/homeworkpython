print('Номер 23')
import re
a='Это строка с большим количеством пробелов.'
res=re.sub(r' +',' ',a)
print(res)
c='   Текст   с   пробелами   '
res2=re.sub(r' +',' ',c).strip()
print(res2)