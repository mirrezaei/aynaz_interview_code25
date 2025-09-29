#Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

#Any live cell with fewer than two live neighbors dies, as if caused by under-population.
#Any live cell with two or three live neighbors lives on to the next generation.
#Any live cell with more than three live neighbors dies, as if by over-population..
#Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

#idea: start traversinng the board, count the neighbors of a node, if it is 1 and is going to die change it to 3
#if it is 0 and is going to live, chnage it to 2
# at the end, traverse the board one more time and change 3 to 0 and 2 to one

class Solution(object):
    def neigh(self, b, i, j):
        countOne = 0
        countZero = 0
        nei = [[-1, 0], [-1, -1], [-1, 1], [0, +1], [0, -1], [1, 0], [1, -1], [1, 1]]
        for n in nei:
            row = n[0] + i
            col = n[1] + j
            if (row >= 0 and row < len(b) and col >= 0 and col < len(b[0])):
                if (b[row][col] == 0 or b[row][col] == 2):
                    countZero += 1
                if (b[row][col] == 1 or b[row][col] == 3):
                    countOne += 1
        return countZero, countOne

    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                zer, one = self.neigh(board, i, j)
                if board[i][j] == 0:# if the current node is 0, change it only when it is going to live
                    if one == 3:
                        board[i][j] = 2
                else:#if current node is 1, change it only when it is going to die
                    if one < 2:#fewer than two live neighbors dies,under-population
                        board[i][j] = 3
                    elif one > 3:#more than three live neighbors dies, as if by over-population
                        board[i][j] = 3
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 2:
                    board[i][j] = 1
                if board[i][j] == 3:
                    board[i][j] = 0
        return board


class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

        visited = set()

        def check(i, j, direction):
            if ((i, j) not in visited):
                visited.add((i, j))
                if (i > 0):
                    up = check(i - 1, j, "u")
                    if (j > 0):
                        upleft = check(i - 1, j - 1, "ul")
                    if (j < len(board[0]) - 1):
                        upright = check(i - 1, j + 1, "ur")
                if (j > 0):
                    left = check(i, j - 1, "l")
                if (i < len(board) - 1):
                    down = check(i + 1, j, "d")
                    if (j < len(board[0]) - 1):
                        downright = check(i + 1, j + 1, "dr")
                    if (j > 0):
                        downleft = check(i + 1, j - 1, "dl")
                if (j < len(board[0]) - 1):
                    right = check(i, j + 1, "r")

                one = 0
                zero = 0
                if (i > 0):
                    if ((board[i - 1][j] == 1 and up == True) or (up == False and board[i - 1][j] == 0)):
                        one += 1
                    else:
                        zero += 1

                    if (j > 0):
                        if ((board[i - 1][j - 1] == 1 and upleft == True) or (
                                upleft == False and board[i - 1][j - 1] == 0)):
                            one += 1
                        else:
                            zero += 1
                    if (j < len(board[0]) - 1):
                        if ((board[i - 1][j + 1] == 1 and upright == True) or (
                                upright == False and board[i - 1][j + 1] == 0)):
                            one += 1
                        else:
                            zero += 1

                if (j > 0):
                    if ((board[i][j - 1] == 1 and left == True) or (left == False and board[i][j - 1] == 0)):
                        one += 1
                    else:
                        zero += 1

                if (i < len(board) - 1):
                    if ((board[i + 1][j] == 1 and down == True) or (down == False and board[i + 1][j] == 0)):
                        one += 1
                    else:
                        zero += 1

                    if (j < len(board[0]) - 1):
                        if ((board[i + 1][j + 1] == 1 and downright == True) or (
                                downright == False and board[i + 1][j + 1] == 0)):
                            one += 1
                        else:
                            zero += 1
                    if (j > 0):
                        if ((board[i + 1][j - 1] == 1 and downleft == True) or (
                                downleft == False and board[i + 1][j - 1] == 0)):
                            one += 1
                        else:
                            zero += 1

                if (j < len(board[0]) - 1):
                    if ((board[i][j + 1] == 1 and right == True) or (right == False and board[i][j + 1] == 0)):
                        one += 1
                    else:
                        zero += 1

                if (board[i][j] == 1):
                    if (one < 2):
                        board[i][j] = 0
                        return False
                    elif (one == 2 or one == 3):
                        return True
                    else:
                        board[i][j] = 0
                        return False
                else:
                    if (one == 3):
                        board[i][j] = 1
                        return False
                    else:
                        return True
            else:
                return True

        check(0, 0, "u")
        return board
s=Solution()
b=[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
print(s.gameOfLife(b))


#2025







