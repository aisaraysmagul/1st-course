class Abaila:
    def __init__(self,san):
        self.san=san
        san=10
        san+=100

'''san=1/2
aaa=Abaila(2)
print(aaa.san)
aaa.san*=san-2
print(aaa.san/2)
print(san)
'''
class A():
    x=1
    def fun(self):
        print('function A')

class B(A):
    x=2

class C(B,A):
    def fun (self):
        print('function C')

a=A()
b=B()
c=C()
print(A)
print(a.x)
print(b.x)
print(c.x)
b.fun()
c.fun()
