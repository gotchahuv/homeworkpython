print('Номер 3')
def pol(text):
    cltx=''
    for c in text.lower():
        if c.isalnum():
            cltx+=c
    print(cltx)
    lt=0
    rt=len(cltx)-1
    while lt<rt:
        if cltx[lt]!=cltx[rt]:
            return False
        lt+=1
        rt-=1
    return True
text=input('Введите текст: ')
print(pol(text))