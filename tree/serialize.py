"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: Node
        :rtype: str
        """
        stack = []
        encode = ""
        if (root == None):
            return encode
        else:
            stack.append("]")
            stack.append(root)
            encode += "["
        while (len(stack) > 0):#DFS approach
            e = stack.pop(-1)
            if (e == "]"):
                encode += e
            else:
                encode += str(e.val) + ","
                if (len(e.children) > 0):
                    stack.append("]")#before adding children of a node we add "]" to the stack
                    encode += "["#before adding children of a node we add "[" to the encode string
                    for ch in e.children:
                        stack.append(ch)
        print(encode)
        return encode

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: Node
        """
        stack = []
        if (data == ""):
            return None
        i = 0
        while (i < len(data)):
            if (data[i] == "["): # start of a level
                stack.append("*")
                i += 1
            elif (data[i] == "]"): #pop all the children at this level and add them to their parent
                q = []
                while (stack[-1] != "*"):
                    node = stack.pop(-1)
                    q.append(node)
                stack.pop(-1)  # should be *
                if (len(stack) == 0):
                    return q[0]
                else:
                    stack[-1].children = q
                    i += 1

            else:#find the value of a node and careat a node for that
                dig = ""
                while (data[i] != ","):
                    dig += data[i]
                    i += 1
                node = Node(int(dig), [])
                stack.append(node)
                i += 1

    # a new approach is a recursive method which seems more pretty
    def recursion(self, root):
        en = str(root.val) + ","
        if (len(root.children) > 0):
            en += "["
            for ch in root.children:
                en += self.recursion(ch)
            en += "]"
        return en

    def serialize2(self, root):# this method keep the order of children from left to righ; however; the stack method keep them in reverse from right to left
        if (root == None):
            return ""
        else:
            out = "[" + str(self.recursion(root)) + "]"
            print(out)
            return out
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))