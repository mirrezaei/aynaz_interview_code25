# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None




class Solution(object):
    def val(self, root, val):
        if (root.left != None):
            leftMax, leftMin, valLeft = self.val(root.left, root.left.val)
        else:
            leftMax, leftMin, valLeft = float("-inf"), float("inf"), True
        if (valLeft == False):
            return 0, 0, False

        if (root.right != None):
            rightMax, rightMin, valRight = self.val(root.right, root.right.val)
        else:
            rightMax, rightMin, valRight = float("-inf"), float("inf"), True
        if (valRight == False):
            return 0, 0, False

        if (val > leftMax and val < rightMin):
            return max(leftMax, rightMax, val), min(leftMin, rightMin, val), True
        else:
            return 0, 0, False

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if (root == None):
            return True
        if (root.left != None):
            leftMax, leftMin, valLeft = self.val(root.left, root.left.val)
        else:
            leftMax, leftMin, valLeft = float("-inf"), float("inf"), True
        if (root.right != None):
            rightMax, rightMin, valRight = self.val(root.right, root.right.val)
        else:
            rightMax, rightMin, valRight = float("-inf"), float("inf"), True
        if (valLeft and valRight and root.val > leftMax and root.val < rightMin):
            return True
        else:
            return False


root=TreeNode(2)
l=TreeNode(1)
r=TreeNode(3)
root.left=l
root.right=r
s=Solution()
s.isValidBST(root)

