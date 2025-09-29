#Given a complete binary tree, count the number of nodes.

#Note:

#Definition of a complete binary tree from Wikipedia:
#In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def dfsTraverse2(self, root):
        if (root == None):
            return 0
        else:
            return self.dfsTraverse(root.right) + self.dfsTraverse(root.left) + 1
    def dfsTraverse(self, root):
        if (root.left == None and root.right == None):
            return 0
        elif (root.left == None):
            return self.dfsTraverse(root.right) + 1
        elif (root.right == None):
            return self.dfsTraverse(root.left) + 1
        else:
            c1 = self.dfsTraverse(root.right) + 1
            c2 = self.dfsTraverse(root.left) + 1
            return c1 + c2

    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if (root == None):
            return 0
        level = 0
        counter = 0
        count = self.dfsTraverse(root)
        print(count + 1)
        return count + 1

