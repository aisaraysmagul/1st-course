import string
def word_count(x):
    file=open(x)
    newfile=''
    a=[]
    filelist=[]
    count=[]
    countwords=0
    countdiff=0
    b=[]
    d=[]
    wordlist=['Сырыма', 'Датова', 'называют', 'предводителем', 'первого', 'освободительного', 'движения', 'в', 'Казахской', 'степи', 'против', 'национального', 'угнетения', 'Его', 'личности', 'посвящено', 'много', 'исследований', 'Однако', 'до', 'сих', 'пор', 'историки', 'спорят', 'о', 'последних', 'годах', 'жизни', 'батыра', 'причинах', 'его', 'смерти', 'и', 'месте', 'захоронения']
    for line in file:
        for i in line:
            if i not in string.punctuation:
                if i not in string.whitespace[1:]:
                    newfile=newfile+i      
    filelist=newfile.split(' ')
    for i in filelist:
        countwords=countwords+1
    print('a)Total number of words in the book:',countwords)
    for k in filelist:
        if k not in a:
            a.append(k)
    for j in a:
        countdiff=countdiff+1
    print('b)Total number of different words:',countdiff)
    for i in filelist:
        count.append(filelist.count(i))
    for l in sorted(zip(count,filelist))[::-1]:
        b.append(l)
    for c,f in b:
        if f not in d:
            d.append(f)
    print('c) 10 most frequently used word in the book:')
    for i in range(10):
        print(d[i])
    print('d)Given a word list, print out all the words in the book that are not in the word list:', end=' ')
    for j in filelist:
        if j not in wordlist:
            print(j, end=' ')
word_count('word.txt')        
