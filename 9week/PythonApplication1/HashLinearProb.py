class LinProbMap:
    def __init__(self):
        self.M = 17                     # 해시 테이블의 크기
        self.table = [None] * self.M    # None: 빈 버킷, -1: 삭제된 버킷

    def hashFn(self, key):              # 제산 함수
        return key % self.M

    # 삽입: 빈 버킷(None) 또는 삭제된 버킷(-1)을 만날 때까지 조사
    def insert(self, key):
        i = self.hashFn(key)
        for _ in range(self.M):
            if self.table[i] is None or self.table[i] == -1:
                self.table[i] = key
                return True
            i = (i + 1) % self.M
        print("테이블이 가득 찼습니다. %d 삽입 실패" % key)
        return False

    # 탐색: None을 만나면 실패, -1은 건너뛰고 계속 조사
    def search(self, key):
        i = self.hashFn(key)
        for _ in range(self.M):
            if self.table[i] is None:
                return None
            if self.table[i] == key:
                return self.table[i]
            i = (i + 1) % self.M
        return None

    # 삭제: 찾은 자리에 -1을 표시해 탐색이 끊기지 않게 함
    def delete(self, key):
        i = self.hashFn(key)
        for _ in range(self.M):
            if self.table[i] is None:
                return False
            if self.table[i] == key:
                self.table[i] = -1
                return True
            i = (i + 1) % self.M
        return False


if __name__ == "__main__":
    # 충돌 테스트: 모두 h(key) = 5
    print("[충돌 테스트]")
    m = LinProbMap()
    for k in [5, 22, 39, 56, 73]:
        m.insert(k)
        print("h(%2d)=%2d" % (k, m.hashFn(k)), m.table)

    # 탐색 및 삭제 테스트
    print("\n[삭제 후 탐색 테스트]")
    m.delete(22)
    m.delete(39)
    print("22, 39 삭제 후:", m.table)
    for k in [22, 39, 5, 56, 73]:
        print("%d탐색-->" % k, m.search(k))
    m.insert(90)    # h(90)=5, 삭제된 자리(-1) 재사용
    print("90 삽입 후:", m.table)

    # 추가 테스트: 10개 이상 삽입 (16, 33, 50은 끝에서 처음으로 돌아감)
    print("\n[추가 테스트]")
    m2 = LinProbMap()
    for k in [16, 33, 50, 1, 18, 7, 24, 12, 29, 3, 40]:
        m2.insert(k)
    print(m2.table)
    for k in [50, 40, 100, 8]:
        print("%d탐색-->" % k, m2.search(k))

    # 테이블이 가득 찬 경우
    print("\n[가득 찬 테이블 테스트]")
    m3 = LinProbMap()
    for k in range(17):
        m3.insert(k)
    print(m3.table)
    m3.insert(100)