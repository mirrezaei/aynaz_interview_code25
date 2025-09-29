# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findNode(self, root, v):
        temp = []
        temp.append(root)

        def dfs(node):
            if (node.val == v):
                return True, temp
            if (node.left != None):
                temp.append(node.left)
                b, pa = dfs(node.left)
                if (b):
                    return b, pa
                else:
                    temp.pop(-1)
            if (node.right != None):
                temp.append(node.right)
                b, pa = dfs(node.right)
                if (b):
                    return b, pa
                else:
                    temp.pop(-1)
            return False, []

        path = dfs(root)
        return path

    def lowestCommonAncestor2(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        _, p1 = self.findNode(root, p.val)
        _, p2 = self.findNode(root, q.val)
        for i in range(min(len(p1), len(p2))):
            if (p1[i].val != p2[i].val):
                break
        return p1[i] if (p1[i].val == p2[i].val) else p1[i - 1]

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        self.common = None

        def dfs(node):# do the post processing
            if node == None:
                return False
            cur = node.val == p.val or node.val == q.val
            lVal = dfs(node.left)
            rVal = dfs(node.right)
            if (cur + lVal + rVal >= 2):
                self.common = node

            return cur or lVal or rVal

        dfs(root)
        return self.common
        # the idea is that during the traversing the graph, each node return a True or False value to its parents
        # this means that if we have seen one of the q or p on left side : lVal is True
        # if we have seen one of the q or p on right side : rVal is True
        # if we have seen one of the q or p on cur node : cur is True
        # the node which has equal or more than two True is the output
