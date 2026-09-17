from ArrayList import ArrayList


class Polynomial:

    def __init__(self, capacity=100):
        # 계수를 저장할 ArrayList. 
        self.coef = ArrayList(capacity)

    def degree(self):
        # 최고 차수 = 저장된 항의 개수 - 1
        return self.coef.size - 1

    def eval(self, scalar):
        # 미지수에 scalar를 대입해서 각 항(계수 * scalar^차수)을 모두 더함
        return sum(self.coef.getEnty(i) * scalar**i for i in range(self.coef.size))

    def add(self, rhs):
        # 두 다항식 중 차수가 더 큰 쪽 길이만큼 반복
        n = max(self.coef.size, rhs.coef.size)
        get = lambda p, i: p.coef.getEnty(i) if i < p.coef.size else 0
        result = Polynomial()
        for i in range(n):
            # 같은 차수끼리 계수를 더해서 새 다항식에 채움
            result.coef.insert(i, get(self, i) + get(rhs, i))
        return result

    def subtract(self, rhs):
        neg = Polynomial()
        for i in range(rhs.coef.size):
            neg.coef.insert(i, -rhs.coef.getEnty(i))
        return self.add(neg)

    def multiply(self, rhs):
        # 곱의 최고차수 
        n = self.coef.size + rhs.coef.size - 1
        result = Polynomial()
        for i in range(n):
            result.coef.insert(i, 0)
        # 모든 항끼리 곱해서 차수가 같은(i+j) 자리에 누적
        for i in range(self.coef.size):
            for j in range(rhs.coef.size):
                cur = result.coef.getEnty(i + j)
                result.coef.replace(i + j, cur + self.coef.getEnty(i) * rhs.coef.getEnty(j))
        return result

    def __str__(self):
        # 계수가 0인 항은 제외하고, 높은 차수부터 낮은 차수 순으로 나열
        terms = [(i, self.coef.getEnty(i)) for i in range(self.coef.size - 1, -1, -1) if self.coef.getEnty(i) != 0]
        if not terms:
            return "0"
        # 차수에 따라 표현 형식을 다르게: x^0은 상수, x^1은 지수 생략
        fmt = lambda i, c: f"{c}" if i == 0 else f"{c} x" if i == 1 else f"{c} x^{i}"
        text = fmt(*terms[0])
        for i, c in terms[1:]:
            part = fmt(i, c)
            # 계수가 음수면 "- 3.0"처럼, 양수면 "+ 3.0"처럼 이어붙임
            text += " - " + part[1:] if part.startswith("-") else " + " + part
        return text

    def display(self, prefix=""):
        print(prefix + str(self))


def read_poly():
    p = Polynomial()
    deg = int(input("다항식의 최고 차수를 입력하시오: "))
    for i in range(deg + 1):
        p.coef.insert(i, float(input(f"x^{i}의 계수 : ")))
    return p


a = read_poly()
b = read_poly()
c = a.add(b)
d = a.multiply(b)
a.display("A(x) = ")
b.display("B(x) = ")
c.display("C(x) = ")
print("C(2) = ", c.eval(2))
d.display("D(x) = A*B = ")