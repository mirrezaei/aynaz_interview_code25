#Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

#Note: You can only move either down or right at any point in time.

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m=len(grid)
        n=len(grid[0])
        minCost=[[0 for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                if(i==0):
                    minCost[i][j]=minCost[i][j-1]+grid[i][j]
                elif(j==0):
                    minCost[i][j]=minCost[i-1][j]+grid[i][j]
                else:
                    minCost[i][j]=min((minCost[i-1][j]+grid[i][j]),(minCost[i][j-1]+grid[i][j]))
        return int(minCost[m-1][n-1])

sol=Solution()
m=[[1,2],[1,1]]
print(sol.minPathSum(m))