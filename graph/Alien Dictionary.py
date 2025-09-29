from collections import defaultdict

#words are sorted lexicographically, print the sorted chars

# first we create a graph from the chars by comparing the pair of words
# we do topological sorting and print the sort; it is a version of dfs approach

# if the graph is DAG -> then just one visited set is enough for topological sorting
# if the the graph may have cycle, then two visited sets are are required
class Solution(object):
    def __init__(self):
        self.out = ""
    def createGraph(self, w, g):
        for i in range(len(w)):
            for ch in w[i]:
                if(ch not in g):
                    g[ch]=[]
        i = 0

        while (i < len(w) - 1):
            if (w[i][0] == w[i + 1][0]):
                j = 0
                while (j < min(len(w[i]), len(w[i + 1])) and w[i][j] == w[i + 1][j]):
                    j += 1
                if (j != min(len(w[i]), len(w[i + 1]))):
                    g[w[i][j]].append(w[i + 1][j])
            else:
                g[w[i][0]].append(w[i + 1][0])
            i += 1

    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        g = defaultdict(list)
        self.createGraph(words, g)
        print(g)
        perVis = set()# if all the children are seen, then add parent to the permanent set
        temVis = set()# when we see a node we add it to the temporal set and after visiting its children we remove it from temporal set; temporal set is used for cycle dtection

        def dfs(n):# we need two visted sets for topological sorting
            if (n in perVis):
                return
            if (n in temVis):
                return True
            temVis.add(n)
            for ch in g[n]:
                if (ch not in perVis):
                    cycle=dfs(ch)
                    if(cycle):
                        return True
            temVis.remove(n)
            perVis.add(n)
            self.out+=n

        for n in g:
            if (n not in perVis):
                cycle = dfs(n)
                if(cycle==True):
                    break
        self.out=self.out[::-1]
        return "" if cycle == True else self.out

s=Solution()
inp=["wrt","wrf", "er", "ett","rftt"]
#inp=["z","x","z"]
#inp=["z","z"]
inp=["ri","xz","qxf","jhsguaw","dztqrbwbm","dhdqfb","jdv","fcgfsilnb","ooby"]
print(s.alienOrder(inp))




