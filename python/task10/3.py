import string
class Student:
    def __init__(self,n,id,g):
        self.name=n
        self.id=id
        self.gpa=g
    def __str__(self):
        return ('%s, ID:%d, GPA:%g'%(self.name,self.id,self.gpa))
def read_from_file(x):
    a=[]
    studlist=[]
    fin=open(x)
    st=[]
    for i in fin:
        a.append(i.split(' '))
    for j in a:
        c=Student(j[1],int(j[0]),float(j[2]))
        studlist.append(c)
    return studlist
def print_list(x):
    b=0
    c=0
    for i in x:
        b=b+1
        print(b,x[c])
        c=c+1

s1=Student('Zamanbek', 77777, 3.99)
print(s1,'\n')
st=read_from_file('Students.txt')
print(st[0])
print_list(st)
#top3(st)
