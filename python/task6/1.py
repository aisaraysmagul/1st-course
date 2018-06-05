ke=dict()
ke['алма']='apple'
ke['тау']='mountain'
ke['шаш']='hair'
def kaz_eng():
    print('Welcome to Kaz-Eng Dictionary!')
    print('==============================','\n','Choose one:')
    print(' 1 - Search','\n','2 - Add','\n','3 - List','\n','4 - Exit')
    print('-------------------')
    x=input('Number of option: ')
    if x=='1':
        y=input('Search:')
        for i in ke:
            if i==y:
                print(ke[i])
        kaz_eng()
    if x=='2':        
        y=input('Please,add new word in Kazakh: ')
        z=input('And its translation in English: ')
        ke[y]=z
        kaz_eng()
    if x=='3':
        print(ke)
        kaz_eng()
    if x=='4':
        print('Good bye!')        
kaz_eng()
    
