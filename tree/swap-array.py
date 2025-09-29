
import math

# swap is too complicated using an array . I couldn't implement it

def traverse(tree,i,res):# only right needs to return, after traversing the whole left, we need to print the node,
    if(tree[2*i]!=-1):
        traverse(tree,2*i,res)
    res.append(tree[i])
    if(tree[2*i+1]==-1):
        return
    else:
        traverse(tree,2*i+1,res)
    return



def swapNodes(indexes, queries):
    tree=[-1,1]
    valMap={}
    valMap[1]=1
    for i in range(1,len(indexes)+1):
        for j in range(len(tree)-1,2*valMap[i]+1):
            tree.append(-1)
        tree[2*valMap[i]]=indexes[i-1][0]
        tree[2*valMap[i]+1]=indexes[i-1][1]
        valMap[indexes[i-1][0]]=2*valMap[i]
        valMap[indexes[i-1][1]]=2*valMap[i]+1

    final=[]
    height=int(math.log(len(tree),2))
    for q in queries:
        res=[]
        k=1
        heights=[]
        while((k*q)<=height):
            heights=heights+[i for i in range(2**((q*k)-1),2**(q*k))]
            k=k+1


        for h in heights:
            if(tree[h]!=-1):
               tmp=tree[2*h]
               tree[2*h]=tree[2*h+1]
               tree[2*h+1]=tmp
        traverse(tree,1,res)
        final.append(res)
    return final






if __name__ == '__main__':
    fptr = open('result.txt', 'w')

    n = int(input())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = swapNodes(indexes, queries)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()
