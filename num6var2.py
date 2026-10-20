print('Номер 6')
from datetime import *
import random
def gen_file(filename):
    a=date(2026, 1, 1)
    with open(filename,'w') as f:
        f.write('date,temp\n')
        for i in range(365):
            day=a+timedelta(days=i)
            temp=random.uniform(-30,30)
            f.write(f'{day},{temp}\n')
def analyz(filename):
    data=[]
    with open(filename,'r') as f:
        for line in f:
            part=line.split(',')
            if len(part)!=2:
                continue
            try:
                day=date.fromisoformat(part[0])
                temp=float(part[1])
            except ValueError:
                continue
            data.append((day,temp))
    if len(data)==0:
        print('no info')
        return
    a=0
    hot=max(data,key=lambda x: x[1])
    cold=min(data,key=lambda x: x[1])
    c=[]
    for i in data:
        a+=i[1]
    avg=a/len(data)
    as1=0
    for i in data:
        if i[1]>avg:
            as1+=1
    maxdif=-1
    data.sort()
    for i in range(1,len(data)):
        day1,temp1=data[i-1]
        day2,temp2=data[i]
        if day2-day1==timedelta(days=1):
            dif=abs(temp2-temp1)
            if dif>maxdif:
                maxdif=dif
    print('avg temp',avg)
    print('max temp',hot)
    print('min temp',cold)
    print('day more avg',as1)
    if maxdif==-1:
        print('No sosed dney')
    else:
        print('Max dif',maxdif)
with open("test.csv", "w") as f:
    f.write("date,temperature\n")
    f.write("2026-01-01,3.5\n")
    f.write("2026-01-02,4.1\n")
    f.write("2026-01-03,-1.0\n")
    f.write("2026-01-04,8.0\n")
    f.write("2026-01-05,0.0\n")
    f.write("error,abc\n")
print('TEST FILE')
analyz("test.csv")
print('GENERATION FILE')
gen_file('temperature.csv')
analyz('temperature.csv')