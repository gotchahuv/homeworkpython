print('НОМЕР 7')
import random
from faker import Faker
def gen_file(filename):
    faker=Faker()
    emails=[]
    for i in range(4000):
        emails.append(faker.email())
    for i in range(1000):
        emails.append(random.choice(emails))
    with open(filename,'w') as f:
        for i in emails:
            f.write(f'{i}\n')
gen_file('email.csv')
def analyz(filename):
    a=set()
    c={}
    repeat=0
    with open(filename,'r') as f:
        for line in f:
            em=line.lower()
            if em in a:
                repeat+=1
                c[em]+=1
            else:
                a.add(em)
                c[em]=1
    mstem=None
    for i in c:
        if mstem is None or c[i]>c[mstem]:
            mstem=i
    print('kol unik adress',len(c))
    print('povt',repeat)
    print('most adress',mstem.strip())
    print('counts most adree',c[mstem])
analyz('email.csv')