#Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
#Integers in each row are sorted in ascending from left to right.
#Integers in each column are sorted in ascending from top to bottom.


#Solution: start from the right top corner
#        or start from the left bottom corner
# we need to start from one of the above options because we have to traverse only one path
#if we start from the right top corner: move down to search greater options.  move left to search smaller numbers


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        i = 0
        if (len(matrix) == 0):
            return False
        j = len(matrix[0]) - 1
        while (i < len(matrix) and j > -1):
            if (target == matrix[i][j]):
                return True
            elif (target > matrix[i][j]):
                i += 1
            else:
                j -= 1

        return False