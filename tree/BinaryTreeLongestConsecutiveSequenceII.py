# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#Given a binary tree, you need to find the length of Longest Consecutive Path in Binary Tree.

#Especially, this path can be either increasing or decreasing. For example, [1,2,3,4] and [4,3,2,1] are both considered valid, but the path [1,2,4,3] is not valid. On the other hand, the path can be in the child-Parent-child order, where not necessarily be parent-child order.

class Solution(object):
    def maxPath(self, root):  # 0->inc ; 1->dec
        if (root.left == None and root.right == None):
            return 1, 1, 1
        inc = 1;
        dec = 1;
        maxPR = 1;
        maxPL = 1
        if (root.left != None):
            incR, decR, maxPR = self.maxPath(root.left)
            if (root.val == root.left.val + 1):
                inc = incR + 1
            if (root.val == root.left.val - 1):
                dec = decR + 1
        if (root.right != None):
            incL, decL, maxPL = self.maxPath(root.right)
            if (root.val == root.right.val + 1):
                inc = max(incL + 1, inc)
            if (root.val == root.right.val - 1):
                dec = max(decL + 1, dec)
        return (inc, dec, max(maxPL, maxPR, inc + dec - 1))

    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if (root == None):
            return 0
        return self.maxPath(root)[2]
