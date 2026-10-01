import os, time, copy, math
from CircularQueue import CircularQueue
from PriorityQueue import PriorityQueue
from ArrayStack import ArrayStack

CAP = 500       # 기본 용량(8, 10)으로는 10x15 미로에서 가득 차므로 크게 지정
DELAY = 0.1





# 미로 (세로 11, 가로 15). e=입구, x=출구, 1=벽, 0=길
ORG = [list(r) for r in [
    "111111111111111",
    "e00010000010001",
    "101010111010101",
    "101000001000101",
    "101111101110101",
    "100000100010001",
    "111110101011101",
    "100010101000001",
    "101110101111101",
    "10000010000000x",
    "111111111111111"]]
H, W = len(ORG), len(ORG[0])
START, EXIT = (0, 1), (14, 9)


def isValidPos(m, x, y):
    return 0 <= x < W and 0 <= y < H and m[y][x] in ('0', 'x')

def euclid(x, y):
    return math.hypot(EXIT[0] - x, EXIT[1] - y)

def manhattan(x, y):
    return abs(EXIT[0] - x) + abs(EXIT[1] - y)


def printMaze(m, info):
    os.system('cls' if os.name == 'nt' else 'clear')
    sym = {'1': '■ ', '.': '√ ', '0': '  ', 'e': '→ ', 'x': '→ ', '★': '★ '}
    for row in m:
        print(''.join(sym[c] for c in row))
    print('현재 위치:', info)


def search(mode):
    m = copy.deepcopy(ORG)
    if mode == 1:   f = ArrayStack(CAP);     put, get = f.push, f.pop
    elif mode == 2: f = CircularQueue(CAP);  put, get = f.enqueue, f.dequeue
    else:           f = PriorityQueue(CAP);  put, get = f.enqueue, f.dequeue

    def item(x, y, g):          # 마지막 3개는 항상 (x, y, g)
        if mode == 3: return (-euclid(x, y), x, y, g)             # 탐욕: 출구와 가까울수록 우선
        if mode == 4: return (-(g + manhattan(x, y)), x, y, g)    # A*: f = g + h
        return (x, y, g)

    put(item(*START, 0))
    printMaze(m, (-1, -1)); time.sleep(DELAY)
    while not f.isEmpty():
        it = get()
        x, y, g = it[-3:]
        if m[y][x] == '.':      # 이미 방문한 칸(중복 삽입) 건너뜀
            continue
        info = (x, y) if mode < 3 else (x, y, round(it[0], 1))
        if m[y][x] == 'x':
            m[y][x] = '★'
            printMaze(m, info)
            return True
        m[y][x] = '.'
        for dx, dy in ((0, -1), (1, 0), (0, 1), (-1, 0)):     # 상 우 하 좌
            if isValidPos(m, x + dx, y + dy):
                put(item(x + dx, y + dy, g + 1))
        printMaze(m, info); time.sleep(DELAY)
    return False


while True:
    c = input('탐색 방법 1=DFS, 2=BFS, 3=PQueue, 4=A*(나의 전략), q=종료 ==> ')
    if c == 'q': break
    if c in ('1', '2', '3', '4'):
        print(' --> 미로탐색 성공' if search(int(c)) else ' --> 미로탐색 실패')


# ---------------- 과제 2: 나의 전략 (A*) 분석 ----------------
# 전략: 우선순위 = -(g + h), g=출발점부터 걸어온 칸 수, h=출구까지의 맨해튼 거리
#   (PriorityQueue가 "큰 값 우선"이라 음수로 넣음)
# 장점: 최단 경로 보장(h가 실제 거리를 넘지 않음). 3번(탐욕)은 막다른 길로 빠질 수 있음.
#       출구 방향이 뻥 뚫린 미로에서는 BFS보다 방문 칸이 훨씬 적음.
# 단점: 출구까지 길이 꼬불꼬불 우회해야 하면 h가 오히려 엉뚱한 방향을 선호해
#       결국 BFS와 비슷하게 많이 탐색. 칸마다 g, h 계산과 PQ 삽입/삭제(O(n)) 비용 발생.