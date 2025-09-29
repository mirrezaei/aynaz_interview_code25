#Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
#For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution(object):
    def buildTree(self, node, l, r, nums):
        if r - l == 1:
            node.val = nums[l]
            return
        if r - l <= 0:
            return
        mid = (r + l) / 2
        node.val = nums[mid]
        if mid - l > 0:
            left = TreeNode()
            node.left = left
            self.buildTree(left, l, mid, nums)
        if r - mid - 1 > 0:
            right = TreeNode()
            node.right = right
            self.buildTree(right, mid + 1, r, nums)
        return

    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) > 0:
            root = TreeNode()
            self.buildTree(root, 0, len(nums), nums)
            return root
        else:
            return None


s=Solution()
nums=[-10,-3,0,5,9]
s.sortedArrayToBST(nums)
