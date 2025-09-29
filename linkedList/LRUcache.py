class LinkedList(object):
    def __init__(self,key):
        self.key=key
        self.next=None
        self.prev=None


#there is a way in pyhon3 ordered dictionary which has a simple solution
#point: when add or remove from the list we should be careful if this is the last element, or first element or in the middle of the lsit
#this is very importnat for both operations

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.d = {}
        self.last = None
        self.first = None
        self.itemNu=0

    def remove(self,node):
        k=node.key
        if(node.next==None):#last element
            if(node.prev!=None):
                node.prev.next=None
                self.last=node.prev
                node.prev=None
            else:#just one element
                self.first=None
                self.last=None
        else:
            if(node.prev!=None):
                node.prev.next=node.next
                node.next.prev=node.prev
            else:#first element
                self.first=node.next
                self.first.prev=None
        return k



    def add(self, node):
        if (self.first == None):#update the last one
            self.last = node
        elif (self.first.next == None):#update the last one
            node.next = self.first
            self.first.prev = node
            self.last = self.first
        else:
            self.first.prev = node
            node.next = self.first
        self.first = node
        self.first.prev=None

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if (key in self.d.keys()):
            node=self.d[key][1]
            self.remove(node)
            self.add(node)
            return self.d[key][0]

        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if(key in self.d.keys()):
            node = self.d[key][1]
            self.remove(node)
            self.add(node)

        else:
            node = LinkedList(key)
            if (self.itemNu < self.capacity):
                self.add(node)
                self.itemNu += 1

            else:
                k = self.remove(self.last)
                del self.d[k]
                self.add(node)
        self.d[key] = [value,node]

# Your LRUCache object will be instantiated and called as such:
obj = LRUCache(3)
# param_1 = obj.get(key)
# obj.put(key,value)
#mode=["LRUCache","put","put","put","put","put","get","put","get","get","put","get","put","put","put","get","put","get","get","get","get","put","put","get","get","get","put","put","get","put","get","put","get","get","get","put","put","put","get","put","get","get","put","put","get","put","put","put","put","get","put","put","get","put","put","get","put","put","put","put","put","get","put","put","get","put","get","get","get","put","get","get","put","put","put","put","get","put","put","put","put","get","get","get","put","put","put","get","put","put","put","get","put","put","put","get","get","get","put","put","put","put","get","put","put","put","put","put","put","put"]
#input=[[10],[10,13],[3,17],[6,11],[10,5],[9,10],[13],[2,19],[2],[3],[5,25],[8],[9,22],[5,5],[1,30],[11],[9,12],[7],[5],[8],[9],[4,30],[9,3],[9],[10],[10],[6,14],[3,1],[3],[10,11],[8],[2,14],[1],[5],[4],[11,4],[12,24],[5,18],[13],[7,23],[8],[12],[3,27],[2,12],[5],[2,9],[13,4],[8,18],[1,7],[6],[9,29],[8,21],[5],[6,30],[1,12],[10],[4,15],[7,22],[11,26],[8,17],[9,29],[5],[3,4],[11,30],[12],[4,29],[3],[9],[6],[3,4],[1],[10],[3,29],[10,28],[1,20],[11,13],[3],[3,12],[3,8],[10,9],[3,26],[8],[7],[5],[13,17],[2,27],[11,15],[12],[9,19],[2,15],[3,16],[1],[12,17],[9,1],[6,19],[4],[5],[5],[8,1],[11,7],[5,2],[9,28],[1],[2,2],[7,4],[4,22],[7,24],[9,26],[13,28],[11,26]]


mode=["LRUCache","put","put","put","put","get","get","get","get","put","get","get","get","get","get"]
input=[[3],[1,1],[2,2],[3,3],[4,4],[4],[3],[2],[1],[5,5],[1],[2],[3],[4],[5]]
for i,m in enumerate(mode):
    if(mode[i]=="put"):
        print(obj.put(input[i][0],input[i][1]))
    if(mode[i]=="get"):
        print(obj.get(input[i][0]))
