from collections import defaultdict
class Solution(object):
    def BFS(self,d,n):
        q=[n]
        obs=set({n})
        while(len(q)>0):
            node=q.pop(0)
            for neigh in d[node]:
                if(neigh not in obs):
                    q.append(neigh)
                    obs.add(neigh)
        return obs


    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        d=defaultdict(list)
        for e in edges:
            if(e[0] not in d):
                d[e[0]]=set()
            if(e[1] not in d):
                d[e[1]]=set()
            d[e[0]].add(e[1])
            d[e[1]].add(e[0])
        observed=set()
        nuComp=0
        for i in range(n):
            if(i not in observed):
                vis=self.BFS(d,i)
                observed=observed.union(vis)
                nuComp+=1
        return nuComp


#n = 5
#edges = [[0, 1], [1, 2], [3, 4]]

#n = 5
#edges = [[0, 1], [1, 2], [2, 3], [3, 4]]

n=4
edges=[[2,3],[1,2],[1,3]]
s=Solution()
print(s.countComponents(n,edges))
