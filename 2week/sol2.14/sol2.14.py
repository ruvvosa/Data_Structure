
endSec = [1200, 4600, 8800, 15000]
tarSec = [0.06, 0.15, 0.24, 0.35]

def calTax(inc):
    tax = 0.0
    i = 1
    if inc > 15000.0:
        tax = (inc - 15000.0) * 0.38
    elif inc <= 1200.0:
        return inc * 0.06
    tax += 1200.0 * 0.06
    while (i < 4):
        if inc > endSec[i]:
            tax += (endSec[i] - endSec[i-1]) * tarSec[i]
            i = i + 1
        else:
            tax += (inc - endSec[i-1]) * tarSec[i]
            return tax
    return tax


print("다음과 같은 세율이 적용됩니다(단위:만원):")
print("~1200:6%, 1200~4600:15%, 4600~8800:24%, 8800~15000:35%, 15000~:38%")
inc = float(input("세전 금액 입력:"))
tax = calTax(inc)
print("세전 : ", inc, "만원")
print("세금 : ", tax, "만원")
print("세후 : ", inc - tax, "만원")
