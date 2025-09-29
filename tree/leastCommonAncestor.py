# Definition for a  binary tree node
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def find(self, A, s, B, found):
        s.append(A.val)
        #print(A.val)
        if (A.val == B):
            found = True
            return found
        if (A.left != None and found == False):
            found=self.find(A.left, s, B, found)
        if (A.right != None and found == False):
            found=self.find(A.right, s, B, found)
        if (found == False):
            del s[-1]
            return False

    def lca(self, A, B, C):
        lca = None
        s1 = []
        found1 = False
        found1=self.find(A, s1, B, found1)
        s2 = []
        found2 = False
        found2=self.find(A, s2, C, found2)
        if (found1 == False or found2 == False):
            return -1
        else:
            for i in range(min(len(s1), len(s2))):
                if (s1[i] == s2[i]):
                    lca = s1[i]
        return lca



tree=TreeNode(1)
#t1=TreeNode(1)
#t2=TreeNode(2)
#tree.left=t1
#tree.right=t2
so=Solution()
lcaVal=so.lca(tree,1,1)
print("LCA: "+str(lcaVal))
