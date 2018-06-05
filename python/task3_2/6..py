
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
    print('a         mysqrt(a)              math.sqrt(a)         diff')
    print(1.0,end='      ')
    print(mysqrt(1),end='                    ')
    print(math.sqrt(1), end='                   ')
    print(abs(mysqrt(1)-math.sqrt(1)))
    print(2.0,end='      ')
    print(mysqrt(2),end='    ')
    print(math.sqrt(2), end='    ')
    print(abs(mysqrt(2)-math.sqrt(2)))
    print(3.0,end='      ')
    print(mysqrt(3),end='   ')
    print(math.sqrt(3), end='    ')
    print(abs(mysqrt(3)-math.sqrt(3)))
    print(4.0,end='      ')
    print(mysqrt(4),end='                  ')
    print(math.sqrt(4), end='                   ')
    print(abs(mysqrt(4)-math.sqrt(4)))
    print(5.0,end='      ')
    print(mysqrt(5),end='     ')
    print(math.sqrt(5), end='      ')
    print(abs(mysqrt(5)-math.sqrt(5)))
    print(6.0,end='      ')
    print(mysqrt(6),end='    ')
    print(math.sqrt(6), end='     ')
    print(abs(mysqrt(6)-math.sqrt(6)))
    print(7.0,end='      ')
    print(mysqrt(7),end='   ')
    print(math.sqrt(7), end='    ')
    print(abs(mysqrt(7)-math.sqrt(7)))
    print(8.0,end='      ')
    print(mysqrt(8),end='     ')
    print(math.sqrt(8), end='    ')
    print(abs(mysqrt(8)-math.sqrt(8)))
    print(9.0,end='      ')
    print(mysqrt(9),end='                  ')
    print(math.sqrt(9), end='                   ')
    print(abs(mysqrt(9)-math.sqrt(9)))
        
test_square_root()
