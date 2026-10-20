print('НОмер2')
def anal():
    maxx=None
    minx=None
    ch=0
    long=0
    pos=0
    while True:
        x=int(input('ЧИСЛО '))
        if x==0:
            break
        if maxx==None or x>maxx:
            maxx=x
        if minx==None or x<minx:
            minx=x
        if x%2==0:
            ch+=1
        if x>0:
            pos+=1
            if pos>long:
                long=pos
        else:
            pos=0
    if minx==None:
        print('no number')
    else:
        print("макс ",maxx)
        print("мин ",minx)
        print("чет ", ch)
        print("макс длина полож ",long)
anal()