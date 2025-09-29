#m=len(workers)
#n=len(bikes)
#n>m
#brute force search: O((n-m)!) -> we need to search all the permutation of assigning bikes to workers
#create a tree, each level of the tree assigns the bike to one specific worker. the height of the tree is at most m
# some parts of the above paths are repeated, so we start traversing the tree with DFS and then keep the state of bike assignments and the workers that have already assigned bikes in a dict.
# the state of bike assignemnts are kept with binary values ; example : n=4; bikeAssign=0110 means bikes 1 and 2 are assigned to some workers
def assignBikes(workers, bikes):
    def dis(i, j):
        return abs(workers[i][0] - bikes[j][0]) + abs(workers[i][1] - bikes[j][1])
    d={}
    def dfs(wr,bikeAssign):# wr is the index of the worker that we want to assign bike to it
        if(wr==len(workers)):
            return 0
        tmp=float('inf')
        for i in range(len(bikes)):
            newPoss=bikeAssign & 1<<i
            newAssign=1<<i|bikeAssign
            if(newPoss==0):
                if((wr+1,newAssign) not in d):
                    tmp=min(tmp,dfs(wr+1,newAssign)+dis(wr,i))
                else:
                    tmp=min(tmp,d[(wr+1,newAssign)]+dis(wr,i))

        d[(wr, bikeAssign)] = tmp
        return tmp


    print(dfs(0,0))
    print(d[(0,0)])



workers = [[0,0],[2,1]]
bikes = [[1,2],[3,3]]

workers = [[0,0],[1,1],[2,0]]
bikes = [[1,0],[2,2],[2,1]]

workers=[[0,0],[1,0],[2,0],[3,0],[4,0]]
bikes=[[0,999],[1,999],[2,999],[3,999],[4,999]]
assignBikes(workers,bikes)