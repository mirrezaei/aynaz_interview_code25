def Neigh():
    return []

def dfs(v):#stack
    visited=set()
    q=[]
    q.append(v)
    while(q):
        node=q.pop(-1)
        if node not in visited:
            visited.add(node)
            for neigh in Neigh(node):
                if neigh not in visited:
                    q.append(neigh)


visited=set()
def dfsRec(v):#recursive
    if v not in visited:
        visited.add(v)
        for node in Neigh(v):
            if node not in visited:
                dfsRec(node)


def dfsCycleDetection(v):
    visited=set()
    path=set()
    q=[]
    q.append(v)
    while(q):
        node=q.pop(-1)
        if node not in visited:
            visited.add(node)
            path.add(node)
            for neigh in Neigh(node):
                if node in path:
                    return True
                if neigh not in visited:
                    q.append(neigh)
            path.remove(node)
    return False

def topologicalSort(v):#a version of dfs, if there is a cycle there is no topologocal test, otherwise, after observing all the children add the node to the output
    visited = set()
    path = set()
    q = []
    q.append(v)
    out=[]
    while (q):
        node = q.pop(-1)
        if node not in visited:
            visited.add(node)
            path.add(node)
            for neigh in Neigh(node):
                if node in path:
                    return True
                if neigh not in visited:
                    q.append(neigh)
            path.remove(node)
            out.append(node)
    return out[::-1]






