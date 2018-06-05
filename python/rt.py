def get_digits(x,y):
    fin=open(x,'r')
    fout=open(y,'w')
    for i in fin:
        for line in i.split():
            print(line)
            a=line.strip(',')
            b=a.strip('.')
            if b.isdigit():
                fout.write(b+'\n')
    fout.close()
get_digits('input.txt','output.txt')
