#A binary tree is a tree which is characterized by one of the following properties:

##It can be empty (null).
#It contains a root node only.
#It contains a root node with a left subtree, a right subtree, or both. These subtrees are also binary trees.
#In-order traversal is performed as

#Traverse the left subtree.
#Visit root.
#Traverse the right subtree.
#For this in-order traversal, start from the left child of the root node and keep exploring the left subtree until you reach a leaf. When you reach a leaf, back up to its parent, check for a right child and visit it if there is one. If there is not a child, you've explored its left and right subtrees fully. If there is a right child, traverse its left subtree then its right in the same manner. Keep doing this until you have traversed the entire tree. You will only store the values of a node as you visit when one of the following is true:

#it is the first node visited, the first time visited
#it is a leaf, should only be visited once
#all of its subtrees have been explored, should only be visited once while this is true
#it is the root of the tree, the first time visited
#Swapping: Swapping subtrees of a node means that if initially node has left subtree L and right subtree R, then after swapping, the left subtree will be R and the right subtree, L.

#For example, in the following tree, we swap children of node 1.


#Conclusion: if we implement this problem with classes then we need to spend time for searching a node in the tree. If we use the array to implement the tree then we need to spend time on the swaping, which is recursive
class TreeNode:
    def __init__(self,nodeValue,height):
        self.nodeValue = nodeValue
        self.left=None
        self.right=None
        self.height=height
    def addChild(self,leftNode,rightNode):
        self.left=leftNode
        self.right=rightNode

    def traverse(self,s):
        if(self.left!=None):
            self.left.traverse(s)
        s.append(self.nodeValue)
        if(self.right==None):
            return
        else:
            self.right.traverse(s)

    def swap(self):
        tmp=self.right
        self.right=self.left
        self.left=tmp

    def searchNode(self,ind): # search a node with a specific value
        if(self.nodeValue==ind):
            return self
        else:
            if(self.left!=None):
                n=self.left.searchNode(ind)
                if(n!=None):
                    return n
            if(self.right!=None):
                n=self.right.searchNode(ind)
                if (n != None):
                    return n
        return None

    def searchHeight(self,h,out): # search nodes with a specific heights
        if (self.height == h):
            out.append(self)
            return out
        if (self.left != None):
            self.left.searchHeight(h,out)
        if (self.right != None):
            self.right.searchHeight(h,out)
        return out

    def startSwapping(self,q):# find nodes that have heights of q multiplication
        if(self.height%q==0 ):
            self.swap()
        if (self.left != None):
            self.left.startSwapping(q)
        if (self.right != None):
            self.right.startSwapping(q)
        return









def swapNodes(indexes, queries):
    head=TreeNode(1,1)
    heighMAp={}
    #construct the tree
    for i,node in enumerate(indexes):
        cur=head.searchNode(i+1)
        if(node[0]!=-1):
            cur.left=TreeNode( node[0],cur.height+1)

        if(node[1]!=-1):
            cur.right=TreeNode( node[1],cur.height+1)
    final=[]
    # for each query swap the tree
    for q in queries:
        nodes = []
        nodesList=head.searchHeight(q,nodes)
        for node in nodesList:
            node.startSwapping(q)
        res=[]
        head.traverse(res)
        final.append(res)

    return final



if __name__ == '__main__':
    fptr = open('result.txt', 'w')

    n = int(input())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = swapNodes(indexes, queries)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()
