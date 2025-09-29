#Suppose we have very large sparse vectors (most of the elements in vector are zeros)



#Two approach
#1) save vectors in dictionaries, key: index, val: value
# find the dot prod, by starting from the smaller dictionary and see if the keys exist in the larger dictionary or not
#2) save them in an array
# save the sparse vectors in array or linked list, indecies should be sorted
#[(1,3),(2,-8),(6,2),(15,-4)]  :# (index,value)
#create two pointers and start traversing the two arrays

def dotProd(a1,a2):
    i=0
    j=0
    out=0
    while i<len(a1) and j<len(a2):
        if a1[i][0]==a2[j][0]:
            out+=a1[i][1]*a2[j][1]
            i+=1
            j+=1
        elif a1[i][0] < a2[j][0]:
            i+=1
        else:
            j+=1

#what if one of the vecots is mych sparser than the other one
def binarySearch(arr,k):
    l=0
    r=len(arr)-1
    while l<=r:
        m = (l+r) / 2
        if arr[m][0]==k:
            return m
        elif arr[m][0]<k:
            l=m+1
        else:
            r=m-1
    return -1

def dotProd(a1,a2):
    out=0
    if len(a1)<len(a2):
        sparse=a1
        large=a2

    else:
        sparse=a2
        large=a1
    for elem in sparse:
        m=binarySearch(large,elem[0])
        if m!=-1:
            out += large[m][1]*elem[1]
    return out

#2025