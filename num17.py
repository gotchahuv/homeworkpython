print('Номер 17')
sum=0
minx=100000
maxx=-100000
c=0
avg=0
with open('numbers17.txt','r',encoding='utf-8') as file:
    for line in file:
        num=int(line)
        sum+=num
        c+=1
        if num<minx:
            minx=num
        if num>maxx:
            maxx=num
    if c!=0:
        avg=sum/c
print(f'{sum}\n{minx}\n{maxx}\n{c}\n{avg}')