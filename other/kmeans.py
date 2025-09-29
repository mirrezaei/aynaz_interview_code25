import random
import math
import sys
inp=[(2,4),(3,5),(8,1),(0,4),(10,2)]
k=2
def distance(x,y):
    return math.sqrt(math.pow(x[0]-y[0],2)+math.pow(x[1]-y[1],2))
def clustering():
    ite=100
    seeds=[[0,0] for i in range(k)]
    #first seeds
    for i in range(k):
        r=random.randint(0,len(inp)-1)
        seeds[i]=inp[r]

    t=0
    inpCluNu = [-1] * len(inp)

    while(t<ite):

        #assignment
        changeAss=False
        for i in range(len(inp)):
            min=sys.maxint
            clusterNu=0
            for j in range(len(seeds)):
                d=distance(inp[1],seeds[j])
                if(d<min):
                    min=d
                    clusterNu=j
            if(clusterNu!=inpCluNu[i]):
                changeAss=True
                inpCluNu[i]=clusterNu

        if(changeAss==False):
            break

        #update
        sum_cent = [[0, 0] for i in range(k)]
        len_cent=[0]*k
        for i in range(len(inp)):
            sum_cent[inpCluNu[i]][0]+=inp[i][0]
            sum_cent[inpCluNu[i]][1]+=inp[i][1]
            len_cent[inpCluNu[i]]+=1

        for i in range(k):
            sum_cent[i][0]=sum_cent[i][0]/len_cent[i]
            sum_cent[i][1]=sum_cent[i][1]/len_cent[i]

        if(seeds==sum_cent):
            break
        else:
            seeds=sum_cent


clustering()





