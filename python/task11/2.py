
class Container:
    def __init__(self,a,b,c):
        self.width=a
        self.length=b
        self.height=c
    def volume(self):
        return(self.width*self.length*self.height)

class Refrigerator(Container):
    def __init__(self,a,b,c,name,f):
        
        super().__init__(a,b,c)
        self.name=name
        self.spec=f
        
    def __str__(self):
        k=0
        q=''
        for i in self.spec.split(','):
            i=self.spec.split(',')[k]
            k=k+1
            q=q+'- '+i+'\n'
        return '%s,%d liters: \n'%(self.name,self.width*self.length*self.height)+q

c = Container(10,20,30)
print(c)
print(c.volume(),'\n')
r = Refrigerator(10,20,30,'Samsung F007','no frost,3 year warranty,rgrd')
print(r)
