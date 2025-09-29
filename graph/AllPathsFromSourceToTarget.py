#Given a directed, acyclic graph of N nodes.  Find all possible paths from node 0 to node N-1, and return them in any order.

#The graph is given as follows:  the nodes are 0, 1, ..., graph.length - 1.  graph[i] is a list of all nodes j for which the edge (i, j) exists.

class Solution(object):
    def allPathsSourceTarget(self, graph):# difference with bfs is that the observed nodes only belong to the current path, not the whole graph
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        q = []
        out = []
        for ch in graph[0]:
            q.append([ch, [0,ch]])
        while (len(q) > 0):
            cur = q.pop(0)
            if (cur[0] == len(graph) - 1):
                out.append(cur[1])
            for ch in graph[cur[0]]:
                    p = list(cur[1])
                    if (ch not in p):
                        p.append(ch)
                        q.append([ch, p])


        print(out)
        return out




    def allPathsSourceTarget2(self, graph):#using dfs and recurssion
        #point in recurssion: never change the path variable, because it is call by reference and will change other things. use path+[ch]
        out=[]

        def find(node, path):
            for ch in graph[node]:
                if (ch == len(graph) - 1):
                    out.append(path+[ch])
                else:
                    if (ch not in path):
                        find(ch, path + [ch])
            return

        find(0,[0])

        print(out)
        return out






s=Solution()
graph=[[1,2], [3], [3], []]
graph=[[4,3,1],[3,2,4],[3],[4],[]]
s.allPathsSourceTarget2(graph)