def grade(x):
    res=0
    for i in sorted(x):
        print(i,':',end=' ')
        y=input()
        res=res+int(y)*x[i]*0.01
    print('-----------')
    print('Total ',res)
    

    
