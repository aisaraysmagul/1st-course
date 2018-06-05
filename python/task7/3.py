def most_frequent(t):
    a=[]
    b=[]
    c=[]
    for i in t:
        a.append(t.count(i))
    for pair in sorted(zip(a,t))[::-1]:
        b.append(pair)
    for k,l in b:
        x=(k/len(t))*100
        if l not in c and (l.islower() or l.isupper()):
            c.append(l)
            print('Frequent of',l,'=',round(x,2),'%')
    print()
most_frequent('Suppose that “ WhatsApp” had a log file for all the messages on your device in the following format:')
def most_frequent_kaz(x):
    a=[]
    b=[]
    c=[]
    g=[]
    e=open(x,encoding='utf-8')
    for i in e:
        d=i.strip()
        a.append(d)
    for j in a:
        for k in j:
            f=j.count(k)
            b.append(f)
    for l in sorted(zip(b,j))[::-1]:
        g.append(l)  
    for t,q in g:
        x=(t/len(j))*100
        if q not in c and (q.islower() or q.isupper()):
            c.append(q)
            print('Frequent of',q,'=',round(x,2),'%')
most_frequent_kaz('kaz.txt')
