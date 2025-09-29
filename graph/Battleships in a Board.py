#Given an 2D board, count how many battleships are in it. The battleships are represented with 'X's, empty slots are represented with '.'s. You may assume the following rules:
#You receive a valid board, made of only battleships or empty slots.
#Battleships can only be placed horizontally or vertically. In other words, they can only be made of the shape 1xN (1 row, N columns) or Nx1 (N rows, 1 column), where N can be of any size.
#At least one horizontal or vertical cell separates between two battleships - there are no adjacent battleships.

class Solution(object):
    def countBattleships2(self, board):# this solution assumes that there is no invalid case as input; otherwise, this solution doesn't work
        # for horizontal cases just considers the first X of the sequence to count and for vertical sequences just consider the last element X to count
        if len(board) == 0: return 0
        m, n = len(board), len(board[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'X' and (i == 0 or board[i - 1][j] == '.') and (j == 0 or board[i][j - 1] == '.'):
                    count += 1
        print(count)
        return count

    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """

        nu = 0

        def dfs(i, j, direction): # the idea is to traverse the sequences depending if it has been through a horizontal or vertical pass previously
            # traverse a sequence  and if the result is not False, then add up the count of battleships
            if (i < 0 or i >= len(board) or j < 0 or j >= len(board[0])):
                return True
            if (board[i][j] == "." or board[i][j] == "F"):
                return True

            if (direction == "h"):
                if (i > 0 and board[i - 1][j] == "X"):
                    return False
                if (i < len(board) - 1 and board[i + 1][j] == "X"):
                    return False
                board[i][j] = "F"
                return dfs(i, j - 1, "h") and dfs(i, j + 1, "h")

            if (direction == "v"):
                if (j > 0 and board[i][j - 1] == "X"):
                    return False
                if (j < len(board[0]) - 1 and board[i][j + 1] == "X"):
                    return False
                board[i][j] = "F"
                return dfs(i - 1, j, "v") and dfs(i + 1, j, "v")

        for i in range(len(board)):
            for j in range(len(board[0])):
                if (board[i][j] == "X"):
                    hl,hr,vu,vd=True,True,True,True
                    if(i>0 and board[i-1][j]=="X"):
                        hl=False
                    if(i<len(board)-1 and board[i+1][j]=="X"):
                        hr=False
                    if(j>0 and board[i][j-1]=="X"):
                        vu=False
                    if(j<len(board[0])-1 and board[i][j+1]=="X"):
                        vd=False
                    if((hl==False or hr==False) and (vu==False or vd==False)):#invalid input
                        return -1

                    if(hl==True and hr==True):
                        if(dfs(i,j,"h")):
                            nu+=1
                        else:
                            return -1
                    else:
                        if (dfs(i, j, "v")):
                            nu += 1
                        else:
                            return -1

        print(nu)
        print(board)
        return nu

s=Solution()
board=[["X","X","X"],["X",".","X"]]
s.countBattleships2(board)