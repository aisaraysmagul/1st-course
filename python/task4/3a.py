def find(word, letter, index):
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1
def count(word, letter):
    x = 0
    index = 0
    while index < len(word):
      nextletter = find(word, letter, index)
      if nextletter != -1:
        x = x + 1
        index = nextletter + 1
      else:
        break
    return x

    

