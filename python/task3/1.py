def sort():
    a=int(input('x= '))
    b=int(input('y= '))
    c=int(input('z= '))
    if a==b==c:
        print('Odered:',a,',',b,',',c)
    else:
        if a<=b and a<=c:
            if b<=c:
                print('Odered:', a,',',b,',',c)
            else:
                print('Odered:', a,',',c,',',b)
        elif b<=a and b<=c:
            if a<=c:
                print('Odered:', b,',',a,',',c)
            else:
                print('Odered:', b,',',c,',',a)
        elif c<=b and c<=a:
            if b<=a:
                print('Odered:',c,',',b,',',a)
            else:
                print('Odered:',c,',',a,',',b)
sort()
