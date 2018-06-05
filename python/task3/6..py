
import math
def mysqrt(a):
    x=a
    while True:
        y = (x + a/x) / 2
        if y == x:
            break
        x = y
    return x
def test_square_root():
    print('a        mysqrt(a)         math.sqrt(a)            diff')
    for i in range (9):
        diff=abs(mysqrt(i+1)-math.sqrt(i+1))
        print(i+1,' ',mysqrt(i+1),(20-int(len(str(mysqrt(i+1)))))*' ',math.sqrt(i+1),(20-int(len(str(math.sqrt(i+1)))))*' ',' '*2,diff)
        
test_square_root()
