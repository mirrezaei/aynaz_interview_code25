from collections import defaultdict
class Solution(object):
    def BFS(self,d,n):

        obs=set({n})
        q=[n]
        while(len(q)>0):
            cur=q.pop()
            for nei in d[cur]:
                if(nei not in obs):
                    q.append(nei)
                    obs.add(nei)
                else:
                    if(cur not in d[nei]):
                        return False,len(obs)
        return  True,len(obs)


    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        d=defaultdict(set)
        if(len(edges)!=n-1):#first check number of edges
            return False
        for e in edges:
            if(e[0] not in d):
                d[e[0]]=set()
            if(e[1] not in d):
                d[e[1]]=set()
            d[e[0]].add(e[1])
            d[e[1]].add(e[0])

        val,vis=self.BFS(d,0)
        if(val==False or vis!=n):
            return False
        return True


n = 5
edges = [[0,1], [0,2], [0,3], [1,4]]
s=Solution()
print(s.validTree(n,edges))