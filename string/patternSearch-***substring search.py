#Suppose you have an array of strings 'src' and a string 'key':

src = {"minecraftgame", "intelligent", "innercrafttalent", "knife", "scissor", "stonecrafter"}
key = "craft"
#Now return all the strings from the 'src' array that contains the key as substring in them. For example, for above case, the solution should be:

#result = {"minecraftgame", innercrafttalent", "stonecrafter"}
# a naive approach is in order of O(n*m)

def search(src,key):#worst case O(n*m)
    out=set()
    key=key+"#"
    for w in src:
        ind = [0]#list of indices of key that we have matched until now
        for i in range(len(w)):
            tmp=[]
            for j in range(len(ind)):
                if(key[ind[j]]==w[i]):
                    tmp.append(ind[j]+1)
                    if(key[ind[j]+1]=="#"):
                        out.add(w)

            tmp.append(0)
            ind=tmp
    return out
def check(key,s):
    return True if s==key else False

def search2(src,key):#Rabin-Karp Algorithm: the worst case is still O(n*m)
    q=11
    d=256
    m=len(key)
    h=pow(d,m-1)%q
    kHash=0
    curHash=0
    out=[]
    for i in range(len(key)):
        kHash=(d*kHash+ord(key[i]))%q

    for w in src:
        curHash=0
        for i in range(m):
            curHash = (d * curHash+ord(w[i]))%q
        for i in range(m,len(w)):
            if(kHash==curHash):
                if(check(key,w[i-m:i])):
                    out.append(w)
                    break
            else:
                curHash=(d*(curHash-ord(w[i-m])*h)+ord(w[i]))%q
                if(curHash<0):
                    curHash+=q
    return out





print(search2(src,key))



