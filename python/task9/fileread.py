import string
def filelis(x):
    file=open(x)
    newfile=''
    filelist=[]
    for line in file:
        for i in line:
            if i not in string.punctuation:
                if i not in string.whitespace[1:]:
                    newfile=newfile+i      
    filelist=newfile.split(' ')
    return filelist
def total_words(x):
    countwords=0
    filelist=filelis(x)
    for i in filelist:
        countwords=countwords+1
    return countwords
def total_diff_words(x):
    filelist=filelis(x)
    countdiff=0
    a=[]
    for k in filelist:
        if k not in a:
            a.append(k)
    for j in a:
        countdiff=countdiff+1
    return countdiff
def most_frequent(x):
    filelist=filelis(x)
    b=[]
    d=[]
    count=[]
    for i in filelist:
        count.append(filelist.count(i))
    for l in sorted(zip(count,filelist))[::-1]:
        b.append(l)
    for c,f in b:
        if f not in d:
            d.append(f)
    print('10 most frequently used word in the book:')
    for i in range(10):
        print(d[i])
def compare_list(x):
    d1=filelis(x)
    d=[]
    d2=open('dict.txt')
    for line in d2:
        d.append(line.strip())
    res=dict()
    for key in d1:
        if key not in d:
            res[key]=None
            if res[key]==None:
                print(key)
