print('Номер 5')
#без нампай
def disp(a):
    n=len(a)
    avg=sum(a)/n
    s=0
    for x in a:
        s+=(x-avg)**2
    gen_var=s/n
    gen_var1=gen_var**0.5
    if n>1:
        svar=s/(n-1)
        svar1=svar**0.5
    return avg,gen_var,gen_var1,svar,svar1

a=[2,4,6,8]
res=disp(a)
print(res)
#с нампай
import numpy as np
print('AVG', np.mean(a))
print('Ген дисп', np.var(a))
print('Ген откл', np.std(a))
print('Выборочная дисперсия', np.var(a,ddof=1))
print('Выборочное отклонение', np.std(a,ddof=1))
#Если мы рассматриваем все элементы из группы то берём n
#Если мы рассматриваем только выборку из большей группы и хотим оценить дисперсию всей генеральной совокупности то берём n-1