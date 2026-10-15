class ArraySet:
    def __init__( self, capacity=100 ):
        self.capacity = capacity
        self.array = [None]*capacity
        self.size = 0

    def isEmpty( self ):
       return self.size == 0

    def isFull( self ):
       return self.size == self.capacity

    def __str__( self ) :
        return str(self.array[0:self.size])

    def contains(self, e) :
        for i in range(self.size) :
            if self.array[i] == e :
                return True
        return False

    def insert(self, e) :
        if not self.contains(e) and not self.isFull() :
           self.array[self.size] = e
           self.size += 1
        else : pass

    def delete(self, e) :
        for i in range(self.size) :
            if self.array[i] == e :
                self.array[i] = self.array[self.size-1]
                self.size -= 1

    def union( self, setB ):
        setC = ArraySet()
        for i in range(self.size) :
            setC.insert(self.array[i])

        for i in range(setB.size) :
            if not setC.contains(setB.array[i]) :
                setC.insert(setB.array[i])

        return setC

    def intersect( self, setB ):            
        setC = ArraySet()
        for i in range(setB.size) :
            if self.contains(setB.array[i]) :
                setC.insert(setB.array[i])
        return setC

    def difference( self, setB ):            
        setC = ArraySet()
        for i in range(self.size) :
            if not setB.contains(self.array[i]) :
                setC.insert(self.array[i])
        return setC


if __name__ == "__main__":
    A = ArraySet()
    B = ArraySet()
    for x in [1, 2, 3, 4]: A.insert(x)
    for x in [3, 4, 5, 6]: B.insert(x)
    print("A =", A)                     
    print("B =", B)                     

    # contains / insert 중복
    print(A.contains(3), A.contains(9))  
    A.insert(3)
    print("중복 insert 후 A =", A)      

    # 집합 연산
    print("A ∪ B =", A.union(B))         
    print("A ∩ B =", A.intersect(B))   
    print("A - B =", A.difference(B))   

    A.delete(2)
    print("delete(2) 후 A =", A)         
    A.delete(99)                       
    print("delete(99) 후 A =", A)         

    C = ArraySet(3)
    print(C.isEmpty())                   # True
    for x in [1, 2, 3, 4]: C.insert(x)   # 4는 무시됨
    print(C, C.isFull())                 # [1, 2, 3] True
