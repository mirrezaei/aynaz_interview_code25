#Given a binary tree, flatten it to a linked list in-place.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        stack = []
        stack.append(root)
        if (root != None):
            while (len(stack) > 0):
                node = stack[-1]
                del stack[-1]
                if (node.right != None):
                    stack.append(node.right)

                if (node.left != None):
                    stack.append(node.left)
                    node.left = None
                    node.right = stack[-1]
                else:
                    if (node.right == None):
                        if (len(stack) > 0):
                            node.right = stack[-1]

        return root