def is_palindrome(x):
    if x[::-1]==x:
        return True
    else:
        return False
is_palindrome('banab')
is_palindrome('neen')
is_palindrome('adaad')
