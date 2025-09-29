# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import sys


class Solution(object):
    def dfs(self, root):
        if (root.left == None and root.right == None):
            return True, 1, root.val, root.val
        elif (root.right == None):
            lVal, ln, maxChild, minChild = self.dfs(root.left)
            # print(str(root.val)+" "+str(ln))
            if (lVal == True and maxChild < root.val):
                return True, ln + 1, max(maxChild, root.val), min(root.val, minChild)
            else:
                return False, ln, 0, 0
        elif (root.left == None):
            rVal, rn, maxChild, minChild = self.dfs(root.right)
            # print(str(root.val)+" "+str(rn))
            if (rVal == True and minChild > root.val):
                return True, rn + 1, max(root.val, maxChild), min(minChild, root.val)
            else:
                return False, rn, 0, 0
        else:
            lVal, ln, maxChild1, minChild1 = self.dfs(root.left)
            rVal, rn, maxChild2, minChild2 = self.dfs(root.right)
            if (lVal == True and rVal == True and maxChild1 < root.val and minChild2 > root.val):
                return True, ln + rn + 1, max(maxChild1, maxChild2, root.val), min(minChild1, minChild2, root.val)
            else:
                return False, max(ln, rn), 0, 0

    def largestBSTSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if (root == None):
            return 0
        validity, num, maxChild, minChild = self.dfs(root)
        print(num)
        return num





