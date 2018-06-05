def find(word, letter, index):
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1
def count2(word,letter):
    count=0
    index=-1
    while index<len(word):
        index=find(word, letter, index+1)
        if index<0:
            break
        count=count+1
    print(count)
    
