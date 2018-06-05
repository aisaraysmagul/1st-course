>>> x='i have a pen, i have an apple'
>>> x.replace('have','pen')
'i pen a pen, i pen an apple'
>>> x.replace('have','had')
'i had a pen, i had an apple'
>>> x='i have have haven haver'
>>> x.replace('have','had',2)
'i had had haven haver'
>>> x.replace('have','had',3)
'i had had hadn haver'
>>> x.replace('have','had',5)
'i had had hadn hadr'
>>> x.replace('have','had',10)
'i had had hadn hadr'
>>> '123'.split(',')
['123']
>>> '1 2 3'.split(',')
['1 2 3']
>>> '1,2,3'.split(',')
['1', '2', '3']
>>> '1 2 3'.split()
['1', '2', '3']
>>> '1.2.3'.split(',')
['1.2.3']
>>> '1.2.3'.split('.')
['1', '2', '3']
>>> x.strip()
'i have have haven haver'
>>> x.strip( )
'i have have haven haver'
>>> x.strip('h')
'i have have haven haver'
>>> 'i have have haven haver'.strip( )
'i have have haven haver'
>>> 'i have have haven haver'.strip('h')
'i have have haven haver'
>>> 'www.example.com'.strip('cmowz.')
'example'
>>> 'ihavehavehavenhaver'.strip('h')
'ihavehavehavenhaver'
>>> comment_string = '#....... Section 3.2.1 Issue #32 .......'
>>> comment_string.strip('.#! ')
'Section 3.2.1 Issue #32'
>>> x='hhoyoyorrr'
>>> x.strip('y')
'hhoyoyorrr'
>>> 'hhoyoyorrr'.strip('yo')
'hhoyoyorrr'
