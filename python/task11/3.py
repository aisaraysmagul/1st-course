def f(word,required):
    return all(letter in word for letter in required)

print(f('carrot','tacrro'))
print(f('carrot','pen'))

def f2(word,forbidden):
    return set(word)<=set(forbidden)

print(f2('car','carrot'))
