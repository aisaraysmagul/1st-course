lisst=['Мен Қазақпын!','Бешбармақ жейдi...','Ұлы жүзге таяқ беріп, малға қой','Орта жүзге қалам беріп, дауға қой','Кіші жүзге найза беріп, жауға қой']
class Qazaq:
    def __init__(self,n=1):
        self.a=lisst[n]
    def __str__(self):
        return lisst[0]
    def ne_isteidi(self):
        print(self.a)
        
class UlyJuz(Qazaq):
    def __init__(self,n=2):
        super().__init__(n)
    
class OrtaJuz(Qazaq):
    def __init__(self,n=3):
        super().__init__(n)

class KiwiJuz(Qazaq):
    def __init__(self,n=4):
        super().__init__(n)
        
qazaq=Qazaq()
print(qazaq)
qazaq.ne_isteidi()
alban = UlyJuz()
qypwaq = OrtaJuz()
aday = KiwiJuz()
alban.ne_isteidi()
qypwaq.ne_isteidi()
aday.ne_isteidi()
halyq = [alban, qypwaq, aday]
for azamat in halyq:
    print(azamat)
