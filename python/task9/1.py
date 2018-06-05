import time
def nm(x):
    fin = open(x,encoding='utf-8')
    ind=0
    s=''
    t=[]
    n=0
    for line in fin:
        for letter in line:
            if letter==']' and ind==1:
                t.append(s)
                s=''
                ind=0
            if letter=='[' and ind==0:
                ind=1
            if ind==1:
                s=s+letter
    for i in t:
        i=i.replace('[','')
        t[n]=i
        n+=1
    return(t)
def form(x):
    fin=open(x,encoding='utf-8')
    a=fin.read()
    t=nm(x)
    t1=tuple()
    q=[]
    q1=[]
    d=dict()
    q0=''
    for i in range(len(t)):
        a=a.replace('['+t[i]+']','%s')
    for i in t:
        for g in i:
            if g==':':
                q=i.split(':')
                for j in q:
                    for l in j:
                        if l==',':
                            q1=j.split(',')
    q0=q[0]+':'+'\n'+q0
    for k in range(4):
        d[k+1]=q1[k]
        q0=q0+str(k+1)+' -'+q1[k]+'\n'
    for i in t:
        if ':'  in i:
            b=input(q0)
            t1+=d[int(b)],        
        elif '#' in i:
            if i.lower()[1]=='d':
                t1+= str(time.strftime('%d.%m.%Y')),
            if i.lower()[1]=='t':
                t1+=str(time.strftime('%H:%M:%S')),
        else:
            b=input(i+': ')
            t1+=b,
    fout=open(t1[0]+'_'+x,'w',encoding='utf-8')
    fout.write(a%t1)
    fout.close()
form('Bank_Request.txt')
 
