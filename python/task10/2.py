class Product:
    def __init__(self,n,p,q=0):
        self.name=n
        self.price=p
        self.quantity=q
        
    def __str__(self):
        return ('%s : %d items x %d tenge' % (self.name,self.quantity,self.price))
    def subtract(self,a):
        self.quantity=self.quantity-a
        return (self.name+' : '+str(self.quantity)+' items'+' x '+str(self.price)+' tenge ')
    def add(self,a):
        self.quantity=self.quantity+a
        return (self.name+' : '+str(self.quantity)+' items'+' x '+str(self.price)+' tenge ')
def print_total(x,sale=0):
    i=0
    total=0
    print('Magnum Kaskelen \nReceipt \n--------')
    for j,k in x:
        i=i+1
        res=j.price*k
        print (str(i)+' '+j.name+'\t'+str(j.price)+' tg x '+str(k)+' = \t'+str(res))
        total=res+total
        j.subtract(k)
    print('=========== \nTotal:',total*(1-(sale/100)))
p1=Product('Tassay 5lt',250,10)
p2 = Product('Aksay Nan', 70, 50)
p3 = Product('Albeni', 110, 35)
p1.subtract(2)
print(p1)
p2.add(10)
print(p2)
product_list = [(p1,2),(p2,3),(p3,5)]
print_total(product_list,20)
print(p1)
        
