# LinkedQueue.py
class Node:
    def __init__ (self, elem, next=None):
        self.data = elem 
        self.link = next


# 코드 6.6: 원형으로 연결된 큐 클래스
class LinkedQueue:
    def __init__( self ):
        self.tail = None

    def isEmpty( self ): return self.tail == None
    def isFull( self ): return False

    def enqueue( self, item ):
        node = Node(item, None)
        if self.isEmpty() :
           self.tail = node
           node.link = node
        else :
            node.link = self.tail.link
            self.tail.link = node
            self.tail = node

    def dequeue( self ):
        if not self.isEmpty():
            data = self.tail.link.data
            if self.tail.link == self.tail : self.tail = None
            else:
                self.tail.link = self.tail.link.link
            return data

    def peek( self ):
        if not self.isEmpty():
            return self.tail.link.data

    def size( self ):
        if self.isEmpty() : return 0
        else :
            count = 1
            node = self.tail.link
            while not node == self.tail :
                node = node.link
                count += 1
            return count

    def __str__( self ):
        arr = []
        if not self.isEmpty() :
            node = self.tail.link
            while not node == self.tail :
                arr.append(node.data)
                node = node.link
            arr.append(node.data)
        return str(arr)


# 너비우선탐색 (BFS)
def BFS(graph, start):
    visited = set([start])
    queue = LinkedQueue()
    queue.enqueue(start)

    while not queue.isEmpty():
        print("큐:", queue)               # 동작 확인용: 현재 큐 상태
        v = queue.dequeue()
        print("방문:", v)
        for w in graph[v]:
            if w not in visited:          # 아직 안 본 인접 정점만 삽입
                visited.add(w)
                queue.enqueue(w)


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
    BFS(graph, 'A')