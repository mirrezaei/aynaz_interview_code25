import numpy as np


class Solution(object):
    def row(self, b, i, ind):
        s = 0
        j = 1
        while (j < len(b[i])):
            if (b[i][j - 1] == b[i][j] and b[i][j]!=0):
                s = j - 1
                j += 1
                if (j >= len(b[i])):
                    break
                while (b[i][j - 1] == b[i][j]):
                    j += 1
                    if (j >= len(b[i])):
                        break
                if (j - s >= 3):
                    for k in range(s, j):
                        ind[i][k] = 1
            else:
                j += 1

    def candyCrush(self, board):
        """
        :type board: List[List[int]]
        :rtype: List[List[int]]
        """
        x = len(board)
        y = len(board[0])
        while (True):
            ind = np.zeros((x, y))
            for i in range(len(board)):
                self.row(board, i, ind)
            prev=np.zeros(len(board[0]))
            ind = np.transpose(ind)
            board = np.transpose(board)
            for i in range(len(board)):
                self.row(board, i, ind)
            for j,col in enumerate(ind):
                i=len(col)-1
                sum=0
                while(i>=0):
                    if(col[i]==1):
                        s=i
                        if(i==0):
                            break
                        while(col[i]==col[i-1] ):
                            i=i-1
                            if(i<=0):
                                break
                        k=i
                        sum = sum + s - k+1
                        for m in range(k, s + 1):
                            ind[j][m] = sum
                        i=i-1
                    else:
                        ind[j][i] = sum
                        i=i-1




            ind = np.transpose(ind)
            board = np.transpose(board)
            if (all(xx==0 for aa in ind for xx in aa)):
                break

            b=board
            for i in range(len(board)-1,-1,-1):
                for j in range(len(board[i])):
                    if (i - ind[i][j] >= 0):
                        #print(shift[j])
                        #print(i-shift[j])
                        board[i][j] = board[int(i -ind[i][j] )][j]
                    else:
                        board[i][j] = 0
        return board


s=Solution()
board = [[110,5,112,113,114],[210,211,5,213,214],[310,311,3,313,314],[410,411,412,5,414],[5,1,512,3,3],[610,4,1,613,614],[710,1,2,713,714],[810,1,2,1,1],[1,1,2,2,2],[4,1,4,4,1014]]
s.candyCrush(board)