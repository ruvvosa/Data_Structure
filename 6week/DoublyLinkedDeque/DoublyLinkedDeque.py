class DNode:
    def __init__ (self, elem, prev, next):
        self.data = elem 
        self.prev = prev
        self.next = next


class DoublyLinkedDeque:
    def __init__( self ):
        self.front = None
        self.rear = None

    def isEmpty( self ): return self.front == None
    def isFull( self ): return False

    def addFront( self, item ):
        node = DNode(item, None, self.front)
        if( self.isEmpty()):
            self.front = self.rear = node
        else :
            self.front.prev = node
            self.front = node

    def addRear( self, item ):
        node = DNode(item, self.rear, None)
        if( self.isEmpty()):
            self.front = self.rear = node
        else :
            self.rear.next = node
            self.rear = node

    def deleteFront( self ):
        if not self.isEmpty():
            data = self.front.data
            self.front = self.front.next
            if self.front==None :
                self.rear = None
            else:
                self.front.prev = None
            return data

    def deleteRear( self ):
        if not self.isEmpty():
            data = self.rear.data
            self.rear = self.rear.prev
            if self.rear==None :
                self.front = None
            else:
                self.rear.next = None
            return data

    def __str__( self ) :
        arr = []
        node = self.front
        while not node == None :
            arr.append(node.data)
            node = node.next
        return str(arr)


# 깊이우선탐색 (DFS): 덱의 후단을 스택으로 사용
def DFS(graph, start):
    visited = set()
    stack = DoublyLinkedDeque()
    stack.addRear(start)                    # push

    while not stack.isEmpty():
        print("스택:", stack)               
        v = stack.deleteRear()              # pop
        if v in visited:
            print("이미 방문:", v)
            continue
        visited.add(v)
        print("방문:", v)
        for w in reversed(graph[v]):        # 역순으로 push해야 작은 정점부터 방문
            if w not in visited:
                stack.addRear(w)            # push


#======================================================================
if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D'],
        'C': ['A', 'D', 'E'],
        'D': ['B', 'C', 'F'],
        'E': ['C', 'F'],
        'F': ['D', 'E'],
    }
    DFS(graph, 'A')