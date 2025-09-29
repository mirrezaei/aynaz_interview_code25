def Neigh():
    return []

def bfs(v):
    q=[]
    visited=set()
    q.append(v)
    visited.add(v)
    while(q):
        node=q.pop(0)
        for nei in Neigh(node):
            if nei not  in visited:
                q.append(nei)
                visited.add(nei)


