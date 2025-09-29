#Given an undirected graph, return true if and only if it is bipartite.

#Recall that a graph is bipartite if we can split it's set of nodes into two independent subsets A and B such that every edge in the graph has one node in A and another node in B.

#The graph is given in the following form: graph[i] is a list of indexes j for which the edge between nodes i and j exists.  Each node is an integer between 0 and graph.length - 1.  There are no self edges or parallel edges: graph[i] does not contain i, and it doesn't contain any element twice.
class Solution(object):

    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        A = set()
        B = set()

        def component(q):
            while (len(q) > 0):
                i = q.pop(0)
                if (i in A):
                    cur = A
                    other = B
                elif (i in B):
                    cur = B
                    other = A
                for n in graph[i]:
                    if (n not in cur and n not in other):
                        q.append(n)
                        other.add(n)
                    elif (n in cur):
                        return False

        for i in range(len(graph)):
            if (i not in A and i not in B):
                q = []
                q.append(i)
                A.add(i)
                res=component(q)
                if(res==False):
                    return False

        print(A)
        print(B)
        return True

inp=[[1,3], [0,2], [1,3], [0,2]]
inp=[[1,2,3],[0,2],[0,1,3],[0,2]]
so=Solution()
so.isBipartite(inp)