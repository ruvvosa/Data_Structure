class Time:
    def __init__(self,h=0,m=0,s=0):
        self.set(h,m,s)


    def set(self,h,m,s): #시각을 h시 m분 s초로 초기화하는 함수
        self.h = h
        self.m = m
        self.s = s
    
    #각 시,분,초를 반환한다
    def hour(self): return self.h
    def minute(self): return self.m
    def second(self): return self.s

    def isAM(self): #시각이 오전이면 true 그렇지 않으면 false
        return self.h <12

    def isSame(self,t): #시간이 t2와 같으면 true 아니면 false
        return self.h==t.h and self.m==t.m and self.s==t.s
    
    def difference(self,t): #t2와의 차이를 새로운 시각에 저장해 반환한다.
        result = Time(self.h - t.h, self.m - t.m, self.s - t.s)
        result.trim()
        return result

    def trim(self):
        self.m += self.s//60
        self.s = self.s % 60
        self.h += self.m//60
        self.m = self.m%60
        self.h = self.h%24
        

    def display(self):
        print("time: %2d:%2d:%2d"%(self.h,self.m,self.s))


  
# 1. 생성자  display 테스트
t1 = Time(9, 30, 0)
print("t1:", end=" ")
t1.display() 

# 2. set 테스트
t2 = Time()
t2.set(15, 45, 10)
print("t2:", end=" ")
t2.display() 

# 3. hour/minute/second 테스트
print("t2 hour:", t2.hour())     
print("t2 minute:", t2.minute()) 
print("t2 second:", t2.second()) 

# 4. isAM 테스트
print("t1 isAM:", t1.isAM()) 
print("t2 isAM:", t2.isAM()) 
# 5. isSame 테스트
t3 = Time(9, 30, 0)
print("t1 isSame t3:", t1.isSame(t3))  
print("t1 isSame t2:", t1.isSame(t2))  

# 6. difference 테스트
t4 = Time(10, 20, 30)
t5 = Time(9, 30, 0)
diff = t4.difference(t5)
print("t4 - t5:", end=" ")
diff.display()  

# 7. trim 테스트 
t6 = Time(10, 23, 61)
t6.trim()
print("10:23:61 trim ->", end=" ")
t6.display()   

t7 = Time(10, -1, 33)
t7.trim()
print("10:-1:33 trim ->", end=" ")
t7.display()   

