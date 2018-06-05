import time
import random
t=[]
f=['From','To']
contact=['Karina','Zhansaya','Mom','Zarina','Beyhan','Aidana','Aldiyar','Abylai',]
for i in range(1000):
    a=random.triangular(1400000000.0,1478202059.0)
    b=str(time.ctime(a))
    c=random.choice(contact)
    e=random.choice(f)
    d=e,c,b
    a=d[0]+' '+d[1]+' '+d[2]
    print(a)
