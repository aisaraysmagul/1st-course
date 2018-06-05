def count_types(*t):
    a=[]
    b=[]
    c=dict()
    for i in t:
        a.append(type(i).__name__)
    for j in a:
        b.append(a.count(j))
    for j,k in sorted(zip(a,b)):
        if j not in c:
            c[j]=k
            print(j,end='')
            print(':','\t',k)
count_types(7,'a',(1,2,3),3.14,2015,'sdu',10010110,3.56,[55,2,7],{1:1,2:4,3:9})
