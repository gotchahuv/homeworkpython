def inter(a,b):
    res=[]
    for x1,x2 in a:
        for y1,y2 in b:
            lt=max(x1,y1)
            rt=min(x2,y2)
            if lt<=rt:
                res.append((lt,rt))
    res.sort()
    ans=[]
    for lt,rt in res:
        if not ans or lt>ans[-1][1]:
            ans.append((lt,rt))
        else:
            ans[-1]=(ans[-1][0], max(ans[-1][1],rt))
    return ans
a = [(1, 5), (10, 15), (20, 25)]
b = [(3, 8), (12, 18), (22, 30)]
print(inter(a, b))