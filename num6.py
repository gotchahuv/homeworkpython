print('номер 6')
from pathlib import Path
k=0#колво файлов
ves=0#mass all files
pyk=0#files with py
dirk=0# count folders
pyl=[]#list of files with py
folder = Path()
for i in folder.rglob('*'):
    k+=1
    ves+=i.stat().st_size
    if i.suffix=='.py':
        pyk+=1
        pyl.append(i)
    if i.is_dir():
        dirk+=1
print(k)
print(ves)
print(pyk)
print(dirk)
for i in pyl:
    print(i)