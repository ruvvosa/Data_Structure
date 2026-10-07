class Node:
    def __init__ (self, elem, link=None):
        self.data = elem 
        self.link = link

class LinkedStack :
    def __init__( self ):
        self.top = None
        self.count = 0

    def isEmpty( self ):
        return self.count == 0

    def push( self, item ):
        self.count += 1
        self.top = Node(item, self.top)

    def peek( self ):
        if not self.isEmpty():
            return self.top.data

    def pop( self ):
        if not self.isEmpty():
            self.count -= 1
            data = self.top.data
            self.top = self.top.link
            return data

    def size( self ):
        return self.count          

    def __str__(self):
        arr = []
        node = self.top
        while not node == None :
            arr.append(node.data)
            node = node.link
        return str(arr)


# 괄호 검사기
def checkBrackets(statement):
    stack = LinkedStack()
    pairs = {')': '(', ']': '[', '}': '{'}

    for ch in statement:
        if ch in "([{":
            stack.push(ch)
        elif ch in ")]}":
            if stack.isEmpty():             
                return False
            if stack.pop() != pairs[ch]:    
                return False

    return stack.isEmpty()                  # 남은 여는 괄호가 없어야 성공


#======================================================================
if __name__ == "__main__":
    
    msg = input("검사할 수식 입력: ")
    print("결과:", "성공" if checkBrackets(msg) else "실패")