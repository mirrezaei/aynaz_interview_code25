#use two indices to find the nodes based on values and heights.

class TreeNode:
    def __init__(self, nodeValue, height):
        self.nodeValue = nodeValue
        self.left = None
        self.right = None
        self.height = height

    def addChild(self, leftNode, rightNode):
        self.left = leftNode
        self.right = rightNode

    def traverse(self, s):
        if (self.left != None):
            self.left.traverse(s)
        s.append(self.nodeValue)
        if (self.right == None):
            return
        else:
            self.right.traverse(s)

    def swap(self):
        tmp = self.right
        self.right = self.left
        self.left = tmp




def startSwapping(q,heighMAp):  # find nodes that have heights of q multiplication
    for i in range(1,max(heighMAp.keys())+1):
        if (i % q == 0):
            for node in heighMAp[i]:
                node.swap()

    return


def swapNodes(indexes, queries):
    head = TreeNode(1, 1)
    heighMAp = {}
    heighMAp[1]=[head]
    valMap={}
    valMap[1]=head
    # construct the tree
    for i, node in enumerate(indexes):
        cur = valMap[i + 1]
        if (node[0] != -1):
            cur.left = TreeNode(node[0], cur.height + 1)
            valMap[node[0]]=cur.left
            if(cur.height+1 not in heighMAp.keys()):
                heighMAp[cur.height + 1]=[]
            heighMAp[cur.height + 1].append(cur.left)
        if (node[1] != -1):
            cur.right = TreeNode(node[1], cur.height + 1)
            valMap[node[1]]=cur.right
            if (cur.height + 1 not in heighMAp.keys()):
                heighMAp[cur.height + 1] = []
            heighMAp[cur.height + 1].append(cur.right)
    final = []
    # for each query swap the tree
    for q in queries:
        startSwapping(q,heighMAp)
        res = []
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
