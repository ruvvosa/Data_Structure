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

    def __sub__( self, rhs ):
        return self.difference(rhs)

    def isProperSubsetOf( self, setB ):
        if self.size >= setB.size :      # 진부분집합이면 A가 B보다 반드시 작아야 함
            return False
        for i in range(self.size) :      # A의 모든 원소가 B에 있는지 확인
            if not setB.contains(self.array[i]) :
                return False
        return True

# 연산자
A = ArraySet(); B = ArraySet()
for x in [1, 2, 3, 4]: A.insert(x)
for x in [3, 4, 5, 6]: B.insert(x)
print("A - B =", A - B)                   
print("B - A =", B - A)                   

# isProperSubsetOf
S = ArraySet(); T = ArraySet(); U = ArraySet()
for x in [1, 2]: S.insert(x)
for x in [1, 2, 3]: T.insert(x)
for x in [2, 1]: U.insert(x)               # S와 같은 집합
print(S.isProperSubsetOf(T))               # 진부분집합
print(S.isProperSubsetOf(U))               # 같은 집합
print(T.isProperSubsetOf(S))               # T가 더 큼
print(A.isProperSubsetOf(B))               # 겹치기만 함