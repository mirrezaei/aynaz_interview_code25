#divide the array into two arrays with equal lenth such that each number appears only one time in the divided array
# numbers are unique

import collections
def reverse():
    n=[2,1,2,3,3,3,4]
    set_a=set()
    set_b=set()

    A=[]
    B=[]
    t=[]
    m=len(n)/2
    d=collections.Counter(n)
    if any(d[k]>2 for k in d):
        return []

    for k in d:
        t.append((k,d[k]))

    t=sorted(t,key=lambda x:x[1],reverse=True)
    print(t)
    i=0
    while(t[i][1]>0):
        num=t[i][0]
        if(num not in set_a and len(A)<m):
            A.append(num)
            set_a.add(num)
            t[i]=(num,t[i][1]-1)
        elif (num not in set_b and len(B) < m):
            B.append(num)
            set_b.add(num)
            t[i] = (num, t[i][1]-1)
        else:
            return []

        t = sorted(t, key=lambda x: x[1], reverse=True)

    print(A)
    print(B)




reverse()





