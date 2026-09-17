class Node:
    def __init__(self, key =0, val =0):
        self.key = key
        self.val =val
        self.next= None
        self.pre =None

class LRU:
    def __init__(self,cap):
        self.cap = cap
        self.key2node = {}
        self.dummy = Node()
        self.dummy.next =self.dummy
        self.dummy.pre = self.dummy

    def get_node(self, key) -> Node:
        if key in self.key2node:
            node = self.key2node[key]
            self.remove(node)
            self.put_front(node)
            self.key2node[key]=node
            return node
        else:
            return None
    def get(self,key) -> int:
        if key not in self.key2node:
            return -1
        else:
            node = self.get_node(key)
            return node.val

    def remove(self,delnode):
        delnode.pre.next = delnode.next
        delnode.next.pre = delnode.pre
        del self.key2node[delnode.key]

    def put(self, key, val):
        #filled

        if key in self.key2node:
            node = self.key2node[key]
            node.val =val
            self.remove(node)
            self.put_front(node)
            self.key2node[key] = node

        else:
            newnode = Node(key,val)
            if len(self.key2node) >= self.cap:
                self.remove(self.dummy.pre)
            self.put_front(newnode)
            self.key2node[key]=newnode
        #not filled
    def put_front(self,node):
        node.next = self.dummy.next
        node.pre = self.dummy
        self.dummy.next.pre =node
        self.dummy.next = node
if __name__=="__main__":
    lru =LRU(2)
    lru.put(1,1)
    lru.put(2,2,)
    print(lru.get(1))
    lru.put(3,3)





