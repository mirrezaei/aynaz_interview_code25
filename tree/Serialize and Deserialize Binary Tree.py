# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


class Codec:

    def recursion(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if (root == None):
            return ""
        elif (root.left == None and root.right == None):
            return (str(root.val) + ",")
        elif (root.left == None and root.right != None):
            return (str(root.val) + "," + "[*" + str(self.recursion(root.right)) + str("]"))
        elif (root.left != None and root.right == None):
            return (str(root.val) + "," + "[" + str(self.recursion(root.left)) + str("*]"))
        else:
            return (str(root.val) + "," + "[" + str(self.recursion(root.left)) + str(self.recursion(root.right)) + "]")

    def serialize(self, root):
        final = self.recursion(root)
        final = "[" + final + "]"
        print(final)
        return final

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        i = 0
        stack = []
        if (data == "[]"):
            return None
        minus = 1
        while (i < len(data)):
            if (data[i] == "["):
                stack.append("[")
                i += 1
            elif (data[i] == "-"):
                minus = -1
                i += 1
            elif (data[i].isdigit()):
                s = ""
                while (data[i].isdigit()):
                    s += data[i]
                    i += 1
                node = TreeNode(int(s) * minus)
                stack.append(node)
                i += 1  # ","
                minus = 1
            elif (data[i] == "*"):
                stack.append(None)
                i += 1

            elif (data[i] == "]"):
                children = []
                while (stack[-1] != "["):
                    children.append(stack.pop(-1))
                stack.pop(-1)  # "["
                if (len(children) == 2):
                    stack[-1].left = children[1]
                    stack[-1].right = children[0]
                    i += 1
                else:
                    return children[0]
        return stack[-1]


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

s=Codec()

n=TreeNode(-1)
l=TreeNode(0)
r=TreeNode(1)
n.right=r
n.left=l

#n=TreeNode(1)
#l=TreeNode(2)
#r=TreeNode(3)
#n.right=r
#n.left=l
#rr=TreeNode(4)
#rl=TreeNode(5)
#r.right=rr
#r.left=rl
#[1,[2,3,[4,5,]]]
final=s.serialize(n)
s.deserialize(final)

# Your Codec object will be instantiated and called as such:
#codec = Codec()
# codec.deserialize(codec.serialize(root))