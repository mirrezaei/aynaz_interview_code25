# directed, undirected representation of graphs
#bfs and dfs traversal

class Graph(object):
    def __init__(self):
        self.adjList={}

    def addEdge(self,node1,node2):
        raise  NotImplementedError

    def bfs(self,node):
        visited=[False for i in range(len(self.adjList.keys()))]
        queue=[]
        bfs=[]
        queue.append(node)
        bfs.append(node)
        while(len(queue)>0):
            visited[queue[0]]=True
            for neigh in self.adjList[queue[0]]:
                if(visited[neigh]==False):
                    queue.append(neigh)
                    visited[neigh]=True
                    bfs.append(neigh)
            del queue[0]
        print(bfs)

    def recurDfs(self,node,visited,dfs):
        for neigh in self.adjList[node]:
            if (visited[neigh] == False):
                dfs.append(neigh)
                visited[neigh]=True
                self.recurDfs(neigh,visited,dfs)
        return (dfs)


    def dfs(self,node):
        visited=[False for i in range(len(self.adjList.keys()))]
        dfs=[]
        visited[node]=True
        dfs.append(node)
        print(self.recurDfs(node,visited,dfs))




class UnDirGraph(Graph):
    def __init__(self):
        super(UnDirGraph, self).__init__()
    def addEdge(self,node1,node2):
        if(node1 not in self.adjList.keys()):
            self.adjList[node1]=[node2]
        else:
            self.adjList[node1].append(node2)

        if (node2 not in self.adjList.keys()):
            self.adjList[node2]=[node1]
        else:
            self.adjList[node2].append(node1)


class DirGraph(Graph):
    def __init__(self):
        super(DirGraph,self).__init__()
    def addEdge(self,node1,node2):
        if (node1 not in self.adjList.keys()):
            self.adjList[node1] = [node2]
        else:
            self.adjList[node1].append(node2)

    def cycle(self,node,visited,stack):
        visited[node]=True
        stack[node]=True
        for neigh in self.adjList[node]:
            if(visited[neigh]==False):
                if(self.cycle(neigh,visited,stack)==True):
                    return True
            else:
                if (stack[neigh] == True):
                    return True
        stack[node]=False
        return False


    def detectCycle(self):
        visited=[False for i in range(len(self.adjList.keys()))]
        stack=[False for i in range(len(self.adjList.keys()))]
        for node in self.adjList.keys():
            if(self.cycle(node,visited,stack)==True):
                return True
        return False


class Graph2():#implemented with lists
    def __init__(self,n):
        self.nuNodes=n
        self.adjList=[[] for i in range(n)]
    def addEdge(self,node1,node2):
        self.adjList[node1].append(node2)
        self.adjList[node2].append(node1)


def createGraph():
    g=DirGraph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)
    return g

g=createGraph()
#g.dfs(0)
#g.bfs(0)
if(g.detectCycle()==True):
    print("Cycle detected")
else:
    print("No cylce")


