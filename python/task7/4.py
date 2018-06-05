def wht_a_and_b(q):
    jt=[]
    at=[]
    bt=[]
    vt=[]
    jf=[]
    af=[]
    bf=[]
    vf=[]
    x=open(q)
    for i in x:
        if i[0]=='T':
            lineto=i.strip()
            jt.append(lineto.split(' '))
        if i[0]=='F':
            linefrom=i.strip()
            jf.append(linefrom.split(' '))
    for l in jt:
        at.append(l[1])
    for c in at:
        bt.append(at.count(c))
    for pair in sorted(zip(bt,at)):
        vt.append(pair)
    d=max(vt)
    print('To:',d[1])
    for l in jf:
        af.append(l[1])
    for c in af:
        bf.append(af.count(c))
    for pair in sorted(zip(bf,af)):
        vf.append(pair)
    d2=max(vf)
    print('From:',d2[1])
def wht_c_i(q):
    x=open(q)
    a=[]
    mon=0
    tue=0
    wed=0
    thu=0
    fri=0
    sat=0
    sun=0
    b=[]
    c=[]
    d=dict()
    for i in x:
        line=i.strip()
        a.append(line.split(' '))
    for k in a:
        for l in k:
            if l=='Mon':
                mon=mon+1
                d['Mon']=mon
            if l=='Tue':
                tue=tue+1
                d['Tue']=tue
            if l=='Wed':
                wed=wed+1
                d['Wed']=wed
            if l=='Thu':
                thu=thu+1
                d['Thu']=thu
            if l=='Fri':
                fri=fri+1
                d['Fri']=fri
            if l=='Sat':
                sat=sat+1
                d['Sat']=sat
            if l=='Sun':
                sun=sun+1
                d['Sun']=sun
    d=d.items()
    d=list(d)
    for l,s in d:
        c.append((s,l))
    for s,l in sorted(c)[::-1]:
        print(l,s)
def wht_c_ii(q):
    x=open(q)
    hours=[]
    for line in x:
        a=line.split()
        b=a[5]
        hour=b[0]+b[1]
        hours.append(hour)
    time=['00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23']
    for i in time:
        print(i,' ',hours.count(i))
def message_stats(q):
    wht_a_and_b(q)
    print('-------------------------')
    wht_c_i(q)
    print('-------------------------')
    wht_c_ii(q)
message_stats('whatsapp.txt')
