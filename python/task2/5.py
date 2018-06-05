import time
t=time.time()
def time():
    d=int(t//(24*3600))
    h=int(t%(24*3600)//3600)
    mi=int(t%3600//60)
    se=int(t%60)
    print('days =',d,h+6,':',mi,':',se)
time()

    
