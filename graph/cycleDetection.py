def Neigh():
    return []

#cycle in directed graph
path=set()
visited=set()
def dfsRec(v):#recursive
    if v not in visited:
        visited.add(v)
        path.add(v)
        for node in Neigh(v):
            if node in path:
                return True
            if node not in visited:
                cycle=dfsRec(node)
                if cycle:
                    return True
        path.remove(v)
    return False


def dfsCycleDetection(v):#stack
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





#cycle in undirected graph
visited=set()
def dfsRec(v):
    if v not in visited:
        visited.add(v)
        for node in Neigh(v):
            if node not in visited:
                cycle=dfsRec(node)
                if cycle:
                    return True
    return False
