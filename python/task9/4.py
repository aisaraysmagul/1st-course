import dbm,pickle,random
db=dbm.open('Studentinfo','c')
def std(x):
    for i in range(x):
        ids=int(input('Student ID: '))
        name=input('Enter Name: ')
        mid1=int(input('MidTerm1: '))
        mid2=int(input('MidTerm2: '))
        fin=int(input('Final: '))
        inf=name,mid1,mid2,fin
        db[str(ids)]=pickle.dumps(inf)
        b=pickle.loads(db[str(ids)])
        t='Name:','MidTerm1:','MidTerm2:','Final'
        for i,name in zip(t,b):
            print(i,'-', name)
    db.close()
