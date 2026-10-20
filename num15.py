print('Номер 15')
from io import StringIO
def count_lines(stream):
    c=0
    for line in stream:
        c+=1
    return c

text=StringIO('Fires\nsec\nthr\nfor')

print(count_lines(text))