class Solution(object):
    def neigh(self, i, j, n, m):
        l = []
        if (i > 0):
            l.append((i - 1, j))
        if (i < n - 1):
            l.append((i + 1, j))
        if (j > 0):
            l.append((i, j - 1))
        if (j < m - 1):
            l.append((i, j + 1))
        return l

    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        if (n > 0):
            m = len(grid[0])
        visited = set()
        q = []
        total = 0# the total number of oranges that should be rotten
        level=0
        for i in range(n):
            for j in range(m):
                if (grid[i][j] == 2):
                    q.append([(i, j), 0])
                    total += 1
                elif (grid[i][j] == 1):
                    total += 1
        while (len(q) > 0):
            cur = q.pop(0)
            cur_node = cur[0]
            if (cur_node not in visited):
                level = cur[1]
                nList = self.neigh(cur_node[0], cur_node[1], n, m)
                for nei in nList:
                    if (nei not in visited and grid[nei[0]][nei[1]] == 1):
                        q.append([nei, level + 1])
                visited.add(cur_node)
        return level if len(visited) == total else -1#




s=Solution()
inp=[[2,1,1],[1,1,0],[0,1,1]]
inp=[[2]]
print(s.orangesRotting(inp))