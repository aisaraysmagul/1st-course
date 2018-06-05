'''def any_lowercase1(s):
for c in s:
if c.islower():
return True
else:
return False'''
def any_lowercase1(s):
    for i in s:
        if s.islower(i):
            return True
        else:
            return False
'''def any_lowercase2(s):
for c in s:
if 'c'.islower():
return 'True'
else:
return 'False' '''
def any_lowercase2(s):
    if s.islower():
        return 'True'
    else:
        return 'False'
