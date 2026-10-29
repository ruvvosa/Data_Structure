class Node:
    def __init__(self, data, link=None):
        self.data = data
        self.link = link


class ChainMap:
    def __init__(self):
        self.M = 17                     # 해시 테이블의 크기
        self.table = [None] * self.M    # 각 버킷은 연결 리스트의 시작 노드

    def hashFn(self, key):              # 제산 함수
        return key % self.M

    # 삽입: 이미 있는 키면 삽입하지 않음
    def insert(self, key):
        if self.search(key) is not None:
            print("%d는 이미 존재합니다. 삽입하지 않습니다." % key)
            return False
        k = self.hashFn(key)
        n = Node(key)
        n.link = self.table[k]          # 새 노드를 리스트의 맨 앞에 연결
        self.table[k] = n
        return True

    def search(self, key):
        n = self.table[self.hashFn(key)]
        while n is not None:
            if n.data == key:
                return n.data
            n = n.link
        return None

    def delete(self, key):
        k = self.hashFn(key)
        n = self.table[k]
        before = None
        while n is not None:
            if n.data == key:
                if before is None:      # 시작 노드 삭제
                    self.table[k] = n.link
                else:                   # 중간/끝 노드 삭제
                    before.link = n.link
                return True
            before = n
            n = n.link
        return False

    def printTable(self):
        for i in range(self.M):
            n = self.table[i]
            print("[%2d] " % i, end='')
            if n is None:
                print("-", end='')
            while n is not None:
                print(n.data, end=' ')
                n = n.link
            print()


if __name__ == "__main__":
    # 충돌 테스트: 모두 h(key) = 5
    print("[충돌 테스트]")
    m = ChainMap()
    for k in [5, 22, 39, 56, 73]:
        m.insert(k)
    m.printTable()

    # 탐색 및 삭제 테스트
    print("\n[삭제 후 탐색 테스트]")
    m.delete(22)     # 리스트 중간 노드
    m.delete(73)     # 리스트 시작 노드 (가장 나중에 삽입됨)
    m.printTable()
    for k in [22, 73, 5, 39, 56]:
        print("%d탐색-->" % k, m.search(k))

    # 중복 삽입 테스트
    print("\n[중복 삽입 테스트]")
    m.insert(5)
    m.insert(56)
    m.printTable()

    # 추가 테스트: 10개 이상 삽입
    print("\n[추가 테스트]")
    m2 = ChainMap()
    for k in [16, 33, 50, 1, 18, 7, 24, 12, 29, 3, 40]:
        m2.insert(k)
    m2.printTable()
    for k in [50, 40, 100, 8]:
        print("%d탐색-->" % k, m2.search(k))
    print("100삭제-->", m2.delete(100))