
def contains(bag,e): #bag에 e가 있는지 여부를 판별하는 함수
    return e in bag

def insert(bag,e): #새로운 항목 e를 넣는 함수
    bag.append(e)

def remove(bag,e): #항목에서 e를 삭제하는 함수
    bag.remove(e)

def count(bag): #bag에 들어 있는 항목의 수를 반환하는 함수
    return len(bag)

def numOf(e,bag):
   return bag.count(e)
   
myBag = []
insert(myBag,'교수님짱')
insert(myBag,'지갑')
insert(myBag,'오이')
insert(myBag,'당근')
insert(myBag,'휴대폰')
insert(myBag,'가지')
print('가방속의 물건',myBag)

insert(myBag,'구름')
remove(myBag,'지갑')
print('가방속의 물건',myBag)
print('항목의 수',numOf('가지',myBag))