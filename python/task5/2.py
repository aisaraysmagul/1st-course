def maxmin(t):
    maxi=t[0]
    index=0
    index_of_maxi=0
    mini=t[0]
    index2=0
    index_of_mini=0
    for i in t:
        if i>maxi:
            maxi=i
            index_of_maxi=index
        index=index+1
        if i<mini:
            mini=i
            index_of_mini=index2
        index2=index2+1
    print ('Max: ',t[index_of_maxi])
    print ('Min: ',t[index_of_mini])


