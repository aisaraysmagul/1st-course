def countdef(word, letter, index):
    count = 0
    for x in word[index:]:
        if x == letter:
            count = count + 1          
    print(count)
    

