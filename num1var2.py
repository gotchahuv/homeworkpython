print('Номер 1')
def matrix(n,m,direc):
    a=[]
    for i in range(n):
        row=[]
        for j in range(m):
            row.append(0)
        a.append(row)
    c=1
    for d in range(n+m-1):
        if direc==1:
            rows=range(n)
        else:
            rows=range(n-1,-1,-1)
        for i in rows:
            j=d-i
            if 0<=j<m:
                a[i][j]=c
                c+=1
    return a
n=int(input())
m=int(input())
direc=int(input())
a=matrix(n,m,direc)
for row in a:
    print(row)