#Given a non-empty binary tree, find the maximum path sum.

#For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root):
            if(root==None):
                return float('-inf'),float('-inf')
            else:
                l,tl=dfs(root.left)
                r,tr=dfs(root.right)
                t=l+r+root.val
                return(max(root.val,l+root.val,r+root.val),max(t,tl,tr,l,r))
        m,n=dfs(root)
        return max(m,n)

#the idea is to traverse the graph in post-order. and when we visit children of a node , we need to return two values:
#1) the maximum value of a path including the current node
#2) the maximum value of a path not necessarily including the current node
#t: max path invovling the node and both children
#tl: max path invovling the node and left child
#tr:max path invovling the node and right child
#l: max path involving the left child
#r: max path involving the right child