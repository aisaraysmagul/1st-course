def word_count():
    y=open('C:/Users/acer e15/Desktop/python/task5/word.txt')
    z=[]
    count=0
    for i in y:
        x=i.strip()
        z.append(x)
        print(x)
        for g in z:
            a=g.split( )
        for j in a:
             count=count+1
    print('Word count: ',count)
def word_count2():
    
    y=open('C:/Users/acer e15/Desktop/python/task5/word.txt')
    z=[]
    count=0
    for i in y:
        x=i.strip()
        z.append(x)
        for g in z:
            a=g.split( )
        for j in a:
            if j=='2' or j=='14':
                count=count
            else:
                count=count+1
    print('Word count: ',count)
