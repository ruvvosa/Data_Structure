from ArrayStack import ArrayStack

def checkBrackets(statement):
    stack = ArrayStack(100)
    line, col = 1, 0

    for ch in statement:
        col += 1
        if ch == '\n':
            line += 1
            col = 0
        elif ch in '{[(':
            stack.push((ch, line, col))       # 위치도 같이 저장
        elif ch in '}])':
            if stack.isEmpty():
                return 3, line, col           # 조건3: 여는 괄호 없이 닫힘
            left, _, _ = stack.pop()
            if ((ch == '}' and left != '{') or
                (ch == ']' and left != '[') or
                (ch == ')' and left != '(')):
                return 2, line, col           # 조건2: 종류 불일치

    if not stack.isEmpty():
        _, l, c = stack.pop()
        return 1, l, c                        # 조건1: 닫히지 않은 여는 괄호
    return 0, 0, 0
    
filename = input("검사할 .py 파일: ")
with open(filename, encoding='utf-8') as f:
    code, line, col = checkBrackets(f.read())

if code == 0:
    print("괄호 검사 통과")
else:
    print(f"에러 {code}: {line}행 {col}번째 문자")