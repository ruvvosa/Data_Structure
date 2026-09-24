
from ArrayStack import ArrayStack

def precedence(op):
    if op in "()":  return 0
    if op in "+-":  return 1
    if op in "*/":  return 2
    return -1

def infix2Postfix(expr):
    s = ArrayStack(100)
    output = []
    for term in expr:
        if term == '(':
            s.push('(')
        elif term == ')':
            while not s.isEmpty():
                op = s.pop()
                if op == '(':
                    break
                output.append(op)
        elif term in "+-*/":
            while not s.isEmpty() and precedence(term) <= precedence(s.peek()):
                output.append(s.pop())
            s.push(term)
        else:
            output.append(term)
    while not s.isEmpty():
        output.append(s.pop())
    return output

def evalPostfix(expr):
    s = ArrayStack(100)
    for token in expr:
        if token in "+-*/":
            val2 = s.pop()
            val1 = s.pop()
            if   token == '+': s.push(val1 + val2)
            elif token == '-': s.push(val1 - val2)
            elif token == '*': s.push(val1 * val2)
            elif token == '/': s.push(val1 / val2)
        else:
            s.push(float(token))
    return s.pop()


# 문제 2(추가)
def tokenize(s):
    tokens = []
    i = 0
    while i < len(s):
        ch = s[i]
        if ch == ' ':
            i += 1
            continue
        prev = tokens[-1] if tokens else None
        # 수식 처음이거나 연산자, '(' 바로 뒤의 +/-는 부호
        is_sign = ch in '+-' and (prev is None or prev in ('+', '-', '*', '/', '('))
        if ch in '+-*/()' and not is_sign:
            tokens.append(ch)
            i += 1
        else:
            j = i + 1 if is_sign else i           # 부호는 숫자에 붙임
            while j < len(s) and (s[j].isdigit() or s[j] == '.'):
                j += 1
            if j == i or s[j-1] in '+-':          # 숫자가 없는 경우
                raise ValueError(f"{i+1}번째 문자 '{ch}' 해석 불가")
            tokens.append(s[i:j])
            i = j
    return tokens

if __name__ == "__main__":
    infix = tokenize(input("입력 수식: "))
    postfix = infix2Postfix(infix)
    print("중위표기:", infix)
    print("후위표기:", postfix)
    print("계산결과:", evalPostfix(postfix))