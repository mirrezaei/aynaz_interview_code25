# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if(root==None):
            return None
        elif(root.left==None and root.right==None):
            return root
        elif(root.left==None):
            temp=TreeNode(root.right.val)
            temp.right=root.right.right
            temp.left=root.right.left
            root.left=temp
            root.right=None
            self.invertTree(root.left)
            return root
        elif(root.right==None):
            temp=TreeNode(root.left.val)
            temp.right=root.left.right
            temp.left=root.left.left
            root.right=temp
            root.left=None
            self.invertTree(root.right)
            return root
        else:
            temp=TreeNode(root.left.val)
            temp.right=root.left.right
            temp.left=root.left.left
            root.left=root.right
            root.right=temp
            self.invertTree(root.left)
            self.invertTree(root.right)
            return root