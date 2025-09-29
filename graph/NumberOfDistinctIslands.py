class Solution2(object):
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        pathSet = set()

        def dfs(i, j, path,cur):
            if (i < len(grid) and i>=0 and j>=0 and j < len(grid[0]) and grid[i][j] == 1):
                grid[i][j] = 2
                path=path+cur
                path = dfs(i, j + 1, path , [1])
                path = dfs(i + 1, j, path , [2])
                path = dfs(i - 1, j, path , [3])
                path = dfs(i, j - 1, path , [4])
                return path+[0]
            else:
                return path

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (grid[i][j] == 1):
                    p = dfs(i, j, [],[0])
                    if (len(p) > 0 and tuple(p) not in pathSet):
                        pathSet.add(tuple(p))

        print(pathSet)
        print(len(pathSet))
        return len(pathSet)


class Solution(object):
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        pathSet = set()

        def dfs(i, j, path, cur):
            if (i < len(grid) and i >= 0 and j < len(grid[0]) and j >= 0 and grid[i][j] == 1):
                grid[i][j] = 2
                path = path + cur
                path = dfs(i, j + 1, path, "r")
                path = dfs(i + 1, j, path, "d")
                path = dfs(i - 1, j, path, "u")
                path = dfs(i, j - 1, path, "l")
                return path+"*"
            else:
                return path

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (grid[i][j] == 1):
                    p = dfs(i, j, "*", "")
                    if (p not in pathSet):
                        pathSet.add(p)

        print(pathSet)
        print(len(pathSet))
        return len(pathSet)


grid=[[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]
grid=[[1,0,1],[0,1,1],[1,1,0]]
grid=[[0,0,1,0,1,0,1,1,1,0,0,0,0,1,0,0,1,0,0,1,1,1,0,1,1,1,0,0,0,1,1,0,1,1,0,1,0,1,0,1,0,0,0,0,0,1,1,1,1,0],[0,0,1,0,0,1,1,1,0,0,1,0,1,0,0,1,1,0,0,1,0,0,0,1,0,1,1,1,0,0,0,0,0,0,0,1,1,1,0,0,0,1,0,1,1,0,1,0,0,0],[0,1,0,1,0,1,1,1,0,0,1,1,0,0,0,0,1,0,1,0,1,1,1,0,1,1,1,0,0,0,1,0,1,0,1,0,0,0,1,1,1,1,1,0,0,1,0,0,1,0],[1,0,1,0,0,1,0,1,0,0,1,0,0,1,1,1,0,1,0,0,0,0,1,0,1,0,0,1,0,1,1,1,0,1,0,0,0,1,1,1,0,0,0,0,1,1,1,1,1,1]]
#grid=[[1,1,0,1,1],[1,0,0,0,1]]
grid=[[0,0,1,0,1,0,1,1,1,0,0,0,0,1,0,0,1,0,0,1,1,1,0,1,1,1,0,0,0,1,1,0,1,1,0,1,0,1,0,1,0,0,0,0,0,1,1,1,1,0],
 [0,0,1,0,0,1,1,1,0,0,1,0,1,0,0,1,1,0,0,1,0,0,0,1,0,1,1,1,0,0,0,0,0,0,0,1,1,1,0,0,0,1,0,1,1,0,1,0,0,0],
 [0,1,0,1,0,1,1,1,0,0,1,1,0,0,0,0,1,0,1,0,1,1,1,0,1,1,1,0,0,0,1,0,1,0,1,0,0,0,1,1,1,1,1,0,0,1,0,0,1,0],
 [1,0,1,0,0,1,0,1,0,0,1,0,0,1,1,1,0,1,0,0,0,0,1,0,1,0,0,1,0,1,1,1,0,1,0,0,0,1,1,1,0,0,0,0,1,1,1,1,1,1]]
s=Solution()
print(len(grid))
for i in range(len(grid)):
    print(grid[i])
s.numDistinctIslands(grid)

