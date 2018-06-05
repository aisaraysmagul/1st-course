def find(word, letter, index, end):   
    while index <= end:
        if word[index] == letter:
            return index
        index = index + 1
    return -1
