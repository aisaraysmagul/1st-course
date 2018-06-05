import random
def makelist(f):
    file = open(f)
    results = []
    for line in file:
        line = line.replace('"', '')
        line = line.strip().split()
        for word in line:
            results.append(word)
    return results
def markov(f, preflen=2):    #f is the file to analyze, preflen is prefix length
     convert_file = makelist(f)
     mapdict = {}        #dict where the prefixes will map to suffixes
     start = 0
     end = preflen         #start/end set the slice size
     for words in convert_file:
         prefix = tuple(convert_file[start:end])     #tuple as mapdict key
         suffix = convert_file[start + 2 : end + 1]  #word as suffix to key
         mapdict[prefix] = mapdict.get(prefix, []) + suffix #append suffixes
         start += 1
         end += 1
     return mapdict
def randsent(f, amt=10):     
    analyze = markov(f)
    a=[]
    for i in range(amt):
        rkey = random.choice(list(analyze))
        print (rkey,analyze[rkey])
